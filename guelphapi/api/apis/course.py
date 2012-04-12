from datetime import datetime

from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpNotFound
from tastypie.resources import Resource
from tastypie.throttle import CacheThrottle

from pyuoguelph import courseparser

class CourseObject(object):
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

class CourseResource(Resource):
    course_code = fields.CharField(attribute='course_code',
            readonly=True, unique=True)
    course_number = fields.CharField(attribute='course_number',
            readonly=True, unique=True)
    course_department = fields.CharField(attribute='course_department',
            readonly=True, unique=True)
    course_title = fields.CharField(attribute='course_title',
            readonly=True, unique=True)
    course_semesters = fields.CharField(attribute='course_semesters',
            readonly=True, unique=True)
    course_credit = fields.CharField(attribute='course_credit',
            readonly=True, unique=True)
    course_description = fields.CharField(attribute='course_description',
            readonly=True, unique=True)
    course_restrictions = fields.CharField(attribute='course_restrictions',
            readonly=True, unique=True)
    course_prereqs = fields.CharField(attribute='course_prereqs',
            readonly=True, unique=True)
    course_uri = fields.CharField(attribute='course_uri',
            readonly=True, unique=True)

    class Meta:
        resource_name = 'course'
        object_class = CourseObject
        allowed_methods = ['get']
        list_allowed_methods = []
        #throttle = BaseThrottle(throttle_at=10)

    def _client(self):
        return courseparser.CourseParser()

    def get_resource_uri(self, bundle_or_obj):
        kwargs = {
            'resource_name': self._meta.resource_name,
        }

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.course_code
        else:
            kwargs['pk'] = bundle_or_obj.couse_code

        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name

        return self._build_reverse_url("api_dispatch_detail", kwargs=kwargs)

    def obj_get(self, request=None, **kwargs):
        year = request.GET.get('year', str(datetime.now().year))
        calendar = request.GET.get('calendar',
                self._client().UNDERGRADUATE_CALENDAR)

        try:
            course = self._client().get_course(year, kwargs['pk'], calendar)
        except courseparser.CourseNotFoundException, e:
            raise ImmediateHttpResponse(HttpNotFound(e.message))

        return CourseObject(initial=course)
