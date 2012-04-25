#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.contrib import admin

from guelphapi.api.models import News, Course, Event
from tastypie.models import ApiKey

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    search_fields = ('user',)
admin.site.register(ApiKey, ApiKeyAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime_published')
    search_fields = ('title', 'category', 'content')
admin.site.register(News, NewsAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'department', 'credit')
    search_fields = ('code', 'title', 'department', 'number', 'description',
            'restrictions', 'prerequisites')
admin.site.register(Course, CourseAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'date')
    search_fields = ('title', 'location', 'organization', 'description')
admin.site.register(Event, EventAdmin)
