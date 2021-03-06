from guelphapi.api.apis.resource import LoggingResource
from guelphapi.api.apis.resource_object import ResourceObject
from guelphapi.api.apis.authentication import BasicHttpApiKeyAuthentication

from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpUnauthorized

from pyuoguelph import mealplanparser

class MealPlanObject(ResourceObject):
    pass

class MealPlanResource(LoggingResource):
    type = fields.CharField(attribute='type')
    balance = fields.CharField(attribute='balance')
    user = fields.CharField(attribute='user')

    class Meta:
        object_class = MealPlanObject
        resource_name = 'mealplan'
        allowed_methods = ['get']
        list_allowed_methods = []
        authentication = BasicHttpApiKeyAuthentication()

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

    def obj_get(self, request=None, **kwargs):
        # Make sure the resource name /schedule/FOO/ is equal to their username
        if kwargs['pk'] != request.user.username:
            raise ImmediateHttpResponse(HttpUnauthorized())

        try:
            parser = mealplanparser.MealPlanParser(request.user.username,
                request.user.password)
            data = parser.get_balance()
        except mealplanparser.InvalidCredentialsException, e:
            raise ImmediateHttpResponse(HttpNotFound(e.message))

        return_object = MealPlanObject(initial=data)
        return_object.user = request.user.username

        return return_object

