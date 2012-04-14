#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.contrib import admin
from guelphapi.api.models import News, Course

admin.site.register(News)
admin.site.register(Course)
