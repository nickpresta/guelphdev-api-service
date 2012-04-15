#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from guelphapi.api.models import Event

import feedparser

from pyuoguelph.eventparser import EventParser

class Command(BaseCommand):
    def handle(self, *args, **options):
        verbosity = int(options.get('verbosity', 1))

        parser = feedparser.parse(settings.EVENTS_FEED_URL)
        event_parser = EventParser()

        num_created = 0
        num_updated = 0
        for entry in parser.entries:
            event = event_parser.get_event(entry.link)
            event['link'] = entry.link
            # The field named "format" causes compatibility issues with Tastypie.
            # Just rename it.
            event['event_format'] = event['format']
            del event['format']
            event, created = Event.objects.get_or_create(**event)
            if created:
                num_created += 1
            else:
                num_updated += 1

        if verbosity > 1:
            sys.stdout.write('Successfully updated %d entries and '
                    'created %d new entries.\n' % (num_updated, num_created))
