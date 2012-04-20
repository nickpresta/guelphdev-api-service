from guelphapi.api.utils.log import get_data

from tastypie.resources import Resource, ModelResource

from mixpanel.tasks import EventTracker

tracker = EventTracker()
track_event = lambda *a, **kw: tracker.run(*a, **kw)

class LoggingResource(Resource):
    def dispatch(self, request_type, request, **kwargs):
        # Let the "real" dispatch do its thing.
        # This includes checking a throttle, authentication, authorization, etc
        response = super(LoggingResource, self).dispatch(request_type, request, **kwargs)
        # Only log "good" requests for now
        # We know once we're down here, that things are fine
        data = get_data(request_type, request, kwargs)
        track_event('request-%s' % request.META.get('REQUEST_METHOD', request_type), data)
        return response

class LoggingModelResource(ModelResource):
    def dispatch(self, request_type, request, **kwargs):
        # Let the "real" dispatch do its thing.
        # This includes checking a throttle, authentication, authorization, etc.
        response = super(LoggingModelResource, self).dispatch(request_type, request, **kwargs)
        # Only log "good" requests for now
        # We know once we're down here, that things are fine
        data = get_data(request_type, request, kwargs)
        track_event('request-%s' % request.META.get('REQUEST_METHOD', request_type), data)
        return response

