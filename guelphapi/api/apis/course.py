from django.conf.urls import url
from guelphapi.api.models import Course

from tastypie.paginator import Paginator
from tastypie.resources import ModelResource

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all().order_by('code')
        resource_name = 'course'
        allowed_methods = ['get']
        list_allowed_methods = ['get']
        paginator_class = Paginator

    #def override_urls(self):
    #    return [
    #            url(r"^(?P<resource_name>%s)/(?P<code>[\w\d]+)/$" % self._meta.resource_name,
    #                self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
    #    ]
