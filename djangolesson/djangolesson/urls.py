from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# This code makes sure that any url starting with 'members' or 'testApp1' will be processed in the urls.py files of the 'members' and 'testApp1' applications. These urls.py files don't originally exist when we make an app within this Django project. We manually added them right after right after listing them here. 

urlpatterns = patterns( '',
    ( r'^$', include( 'home.urls' ) ),
    ( r'^members/', include( 'members.urls' ) ),
    ( r'^testApp1/', include( "testApp1.urls" ) ),
    ( r'^anotherapp/', include( "anotherapp.urls" ) ),
    ( r'^admin/', include( admin.site.urls ) ),
    
    # Examples:
    # url(r'^$', 'djangolesson.views.home', name='home'),
    # url(r'^djangolesson/', include('djangolesson.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 )

