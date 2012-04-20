from guelphapi.api.apis.resource import LoggingResource

from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.bundle import Bundle
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpNotFound
from tastypie.resources import Resource

from pyuoguelph import mealplanparser

class MealPlanObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data

class MealPlanResource(LoggingResource):
    type = fields.CharField(attribute='type')
    balance = fields.CharField(attribute='balance')
    user = fields.CharField(attribute='user')

    class Meta:
        object_class = MealPlanObject
        resource_name = 'mealplan'
        allowed_methods = ['post']
        list_allowed_methods = ['post']
        authorization = DjangoAuthorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True

    def get_resource_uri(self, bundle_or_obj):
        kwargs = {
            'resource_name': self._meta.resource_name,
        }

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.user
        else:
            kwargs['pk'] = bundle_or_obj.user

        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name

        return self._build_reverse_url("api_dispatch_detail", kwargs=kwargs)

    def obj_create(self, bundle, request=None, **kwargs):
        data = self.deserialize(request, request.raw_post_data,
                format=request.META.get('CONTENT_TYPE', 'application/json'))
        try:
            parser = mealplanparser.MealPlanParser(data.get('user', ''),
                data.get('password', ''))
            data = parser.get_balance()
        except mealplanparser.InvalidCredentialsException, e:
            raise ImmediateHttpResponse(HttpNotFound(e.message))

        bundle.obj = MealPlanObject(initial=data)
        bundle = self.full_hydrate(bundle)

        return bundle

    def post_list(self, request, **kwargs):
        response = super(MealPlanResource, self).post_list(request,  **kwargs)
        if 'Location' in response:
            del response['Location']
        return response

    def dehydrate(self, bundle):
        del bundle.data['password']
        del bundle.data['user']
        del bundle.data['resource_uri']

        return bundle
