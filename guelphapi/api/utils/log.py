#!/usr/bin/env python
#-*- coding: utf-8 -*-

from guelphapi.api.utils.ip import get_client_ip

from tastypie.serializers import Serializer

def get_data(request_type, request, kwargs):
    data = {}

    data['distinct_id'] = request.GET.get('api_key', '')
    data['ip'] = get_client_ip(request)
    data['mp_name_tag'] = request.GET.get('username', '')
    data['type'] = request_type.upper()
    data['method'] = request.META.get('REQUEST_METHOD', '')
    data['path'] = request.path
    data['api_name'] = kwargs.get('api_name', '')
    data['resource_name'] = kwargs.get('resource_name', '')
    data['user_agent'] = request.META.get('HTTP_USER_AGENT', '')
    data['accept'] = request.META.get('HTTP_ACCEPT', '')
    data['mp_note'] = "%s request on %s" % (data['method'], data['path'])

    return data
