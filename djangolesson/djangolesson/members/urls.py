'''
Created on Jul 23, 2011

@author: williamclaiborne
'''

from django.conf.urls.defaults import *

urlpatterns = patterns( 'members.views',
                       ( r'^list', 'membersList' ),
                       ( r'^$', 'myFirstView' ),
                       ( r'^betterList$', 'betterMembersList' ),
                       ( r'^formView$', 'formView' ),
                       )

'''
djangoles-tutorial.pdf says (paraphrased):

This file looks just like the first `urls.py`. Note, however,
that we used the first argument of the `patterns` command to tell we
will use views located in `members/views.py`. 


What the hell is a view, again? 
=> A function that takes in some data like a URL, form input, logged in user, 
etc... and returns an HTTP compatible message. 

`HttpResponse` is a simple example of a function that returns such a message.
'''



