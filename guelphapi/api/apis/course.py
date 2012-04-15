from django.conf.urls import url
from guelphapi.api.models import Course

from tastypie.authentication import ApiKeyAuthentication
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all().order_by('code')
        resource_name = 'course'
        allowed_methods = ['get']
        list_allowed_methods = ['get']
        paginator_class = Paginator
        #authentication = ApiKeyAuthentication()

