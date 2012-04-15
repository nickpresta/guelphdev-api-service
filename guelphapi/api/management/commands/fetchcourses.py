#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from guelphapi.api.models import Course

from bs4 import BeautifulSoup

from pyuoguelph.courseparser import CourseParser

class Command(BaseCommand):
    def handle(self, *args, **options):
        verbosity = int(options.get('verbosity', 1))

        num_created = 0
        num_updated = 0
        for code in settings.COURSE_PROGRAM_CODES:
            source = CourseParser._fetch_source(
                    settings.COURSE_PROGRAM_ROOT_URL % code)
            soup = BeautifulSoup(source)
            courses_source = soup.find_all('div', {'class': 'course'})
            for course_s in courses_source:
                c = CourseParser.parse_source(str(course_s))
                course, created = Course.objects.get_or_create(code=c['course_code'],
                    defaults={
                        'number': c['course_number'],
                        'department': c['course_department'],
                        'title': c['course_title'],
                        'semesters': c['course_semesters'],
                        'credit': c['course_credit'],
                        'description': c['course_description'],
                        'restrictions': c['course_restrictions'],
                        'prerequisites': c['course_prereqs']
                    })
                if created:
                    num_created += 1
                else:
                    num_updated += 1

        if verbosity > 1:
            sys.stdout.write('Successfully updated %d entries and '
                    'created %d new entries.\n' % (num_updated, num_created))
