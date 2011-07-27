'''
Created on Jul 25, 2011

@author: williamclaiborne
'''
from django.conf.urls.defaults import *

urlpatterns = patterns( 'home.views',
                        ( r'^$', 'printWelcome' ),
                       )

''' The same from members.urls:

from django.conf.urls.defaults import *

urlpatterns = patterns( 'members.views',
                       ( r'^list', 'membersList' ),
                       ( r'^$', 'myFirstView' ),
                       ( r'^betterList$', 'betterMembersList' ),
                       ( r'^formView$', 'formView' ),
                       )

'''
