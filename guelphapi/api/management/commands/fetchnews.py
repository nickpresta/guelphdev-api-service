#!/usr/bin/env python
#-*- coding: utf-8 -*-

import HTMLParser
import sys

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_unicode
from django.utils.html import strip_tags
from guelphapi.api.models import News

from dateutil import parser
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

def _build(entry):
    d = {}
    d['title'] = entry.title
    d['datetime_published'] = parser.parse(entry.published)
    d['link'] = entry.link
    d['content'] = convert_smart_quotes(
            HTMLParser.HTMLParser().unescape(
                strip_tags(
                    entry.summary).strip()))
    try:
        d['category'] = entry.tags[0].term
    except IndexError:
        d['category'] = ''
    return d

class Command(BaseCommand):
    def handle(self, *args, **options):
        verbosity = int(options.get('verbosity', 1))

        parser = feedparser.parse(settings.NEWS_FEED_URL)

        num_created = 0
        num_updated = 0
        for entry in parser.entries:
            d = _build(entry)
            news, created = News.objects.get_or_create(link=d['link'],
                defaults={
                    'title': d['title'],
                    'datetime_published': d['datetime_published'],
                    'content': d['content'],
                    'category': d['category']
                })
            if created:
                num_created += 1
            else:
                num_updated += 1

        if verbosity > 1:
            sys.stdout.write('Successfully updated %d entries and '
                    'created %d new entries.\n' % (num_updated, num_created))

