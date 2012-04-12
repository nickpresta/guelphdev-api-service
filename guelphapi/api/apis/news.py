import HTMLParser

from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_unicode
from django.utils.html import strip_tags

from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpNotFound
from tastypie.resources import Resource
from tastypie.throttle import CacheThrottle

import feedparser

# translation mapping table that converts
# single/double smart quote characters to standard
# single/double quotes
SINGLE_QUOTE_MAP = {
    0x2018: 39,
    0x2019: 39,
    0x201A: 39,
    0x201B: 39,
    0x2039: 39,
    0x203A: 39,
}

DOUBLE_QUOTE_MAP = {
    0x00AB: 34,
    0x00BB: 34,
    0x201C: 34,
    0x201D: 34,
    0x201E: 34,
    0x201F: 34,
}

def convert_smart_quotes(s):
    return smart_unicode(s).translate(
            DOUBLE_QUOTE_MAP).translate(SINGLE_QUOTE_MAP)

class NewsObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data

class NewsResource(Resource):
    news_id = fields.CharField(attribute='news_id',
            readonly=True, unique=True)
    news_title = fields.CharField(attribute='news_title',
            readonly=True)
    news_date = fields.CharField(attribute='news_date',
            readonly=True)
    news_link = fields.CharField(attribute='news_link',
            readonly=True, unique=True)
    news_content = fields.CharField(attribute='news_content',
            readonly=True)
    news_category = fields.CharField(attribute='news_category',
            readonly=True)

    class Meta:
        resource_name = 'news'
        object_class = NewsObject
        allowed_methods = ['get']
        list_allowed_methods = ['get']
        #throttle = BaseThrottle(throttle_at=10)

    @staticmethod
    def _build_object(entry):
        obj = NewsObject()
        obj.news_id = slugify(entry.id)
        obj.news_title = entry.title
        obj.news_date = entry.published
        obj.news_link = entry.link
        obj.news_content = convert_smart_quotes(
                HTMLParser.HTMLParser().unescape(
                    strip_tags(
                        entry.summary).strip()))
        try:
            obj.news_category = entry.tags[0].term
        except IndexError:
            obj.news_category = ''
        return obj


    def get_resource_uri(self, bundle_or_obj):
        kwargs = {
            'resource_name': self._meta.resource_name,
        }

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = slugify(bundle_or_obj.obj.news_id)
        else:
            kwargs['pk'] = slugify(bundle_or_obj.news_id)

        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name

        return self._build_reverse_url("api_dispatch_detail", kwargs=kwargs)

    def get_object_list(self, request):
        parser = feedparser.parse(settings.NEWS_FEED_URL)
        results = []

        for entry in parser.entries:
            results.append(self._build_object(entry))

        return results

    def obj_get_list(self, request=None, **kwargs):
        return self.get_object_list(request)

    def obj_get(self, request=None, **kwargs):
        parser = feedparser.parse(settings.NEWS_FEED_URL)

        for entry in parser.entries:
            if slugify(entry.id) == kwargs['pk']:
                return self._build_object(entry)

        raise ImmediateHttpResponse(HttpNotFound('News item not found'))

