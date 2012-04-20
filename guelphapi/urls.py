from django.conf import settings
from django.conf.urls import patterns, include, url

from tastypie.api import Api
from api.apis.course import CourseResource
from api.apis.news import NewsResource
from api.apis.event import EventResource
from api.apis.mealplan import MealPlanResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CourseResource())
v1_api.register(NewsResource())
v1_api.register(EventResource())
v1_api.register(MealPlanResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    # Examples:
    # url(r'^$', 'guelphapi.views.home', name='home'),
    # url(r'^guelphapi/', include('guelphapi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
)
