from guelphapi.api.models import Course
from guelphapi.api.apis.resource import LoggingModelResource

from tastypie.authentication import ApiKeyAuthentication
from tastypie.paginator import Paginator

class CourseResource(LoggingModelResource):
    class Meta:
        queryset = Course.objects.all().order_by('code')
        resource_name = 'course'
        allowed_methods = ['get']
        list_allowed_methods = ['get']
        paginator_class = Paginator
        authentication = ApiKeyAuthentication()

