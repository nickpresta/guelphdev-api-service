from guelphapi.api.models import Event

from tastypie.authentication import ApiKeyAuthentication
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        allowed_methods = ['get']
        list_allowed_methods = ['get']
        paginator_class = Paginator
        #authentication = ApiKeyAuthentication()

