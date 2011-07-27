'''
Created on Jul 23, 2011

@author: williamclaiborne
'''

from django.conf.urls.defaults import *

urlpatterns = patterns( 'testApp1.views',
                       ( r'', 'testApp1_view1' ),
                        )

''' Notes:
The first arg ( 'testapp1.views' ) is the location of the views 
    that we want executed.
The second arg ( ( r'', 'testApp1_view1' ) ) says that we'll use 
    the function 'testApp1_view1' for every URL.
    
The project urls.py file is where we defined how the url would 
    start, namely with 'testApp1/'. 
'''


''' Recall urls.py for the main project:

urlpatterns = patterns( '',
    ( r'^members/', include( "members.urls" ) ),
    ( r'^testApp1/', include( "testApp1.urls" ) )
    # Examples:
    # url(r'^$', 'djangolesson.views.home', name='home'),
    # url(r'^djangolesson/', include('djangolesson.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 )
 
'''
