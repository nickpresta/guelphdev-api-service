from guelphapi.api.models import News
from guelphapi.api.apis.resource import LoggingModelResource

from tastypie.authentication import ApiKeyAuthentication
from tastypie.paginator import Paginator

class NewsResource(LoggingModelResource):
    class Meta:
        queryset = News.objects.all().order_by('-datetime_published')
        resource_name = 'news'
        allowed_methods = ['get']
        list_allowed_methods = ['get']
        paginator_class = Paginator
        authentication = ApiKeyAuthentication()
        filtering = {
            'datetime_published': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'category': ['exact', 'iexact', 'contains', 'icontains'],
        }

