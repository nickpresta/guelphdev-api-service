#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'guelphapi')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'guelphapi.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
