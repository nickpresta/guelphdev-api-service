from guelphapi.api.models import Event
from guelphapi.api.apis.resource import LoggingModelResource

from tastypie.authentication import ApiKeyAuthentication
from tastypie.paginator import Paginator

class EventResource(LoggingModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        allowed_methods = ['get']
        list_allowed_methods = ['get']
        paginator_class = Paginator
        authentication = ApiKeyAuthentication()

