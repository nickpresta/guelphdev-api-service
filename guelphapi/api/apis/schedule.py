from subprocess import check_output

from guelphapi.api.apis.resource import LoggingResource
from guelphapi.api.apis.resource_object import ResourceObject
from guelphapi.api.apis.authentication import BasicHttpApiKeyAuthentication

from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpUnauthorized

from pyuoguelph import scheduleparser

class ScheduleObject(ResourceObject):
    pass

class ScheduleResource(LoggingResource):
    schedule = fields.ListField(attribute='schedule')
    user = fields.CharField(attribute='user')

    class Meta:
        object_class = ScheduleObject
        resource_name = 'schedule'
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

        output = '1|ANTH*1150*01|2012/01/09|2012/04/20|LEC|Tues, Thur |10:00AM - 11:20AM|ROZH, Room 101,1|ANTH*1150*01|2012/04/19|2012/04/19|EXAM|Thur |07:00PM - 09:00PM|ROZH, Room 101,2|PHIL*2140*DE|2012/01/09|2012/04/20|Distance Education|Days TBA|Times TBA|Room TBA,2|PHIL*2140*DE|2012/04/18|2012/04/18|EXAM|Wed |11:30AM - 01:30PM|MACN, Room 113'

        parser = scheduleparser.ScheduleParser()
        schedule = parser.get_schedule(output)

        return_object = ScheduleObject(initial=schedule)
        return_object.user = request.user.username

        return return_object

