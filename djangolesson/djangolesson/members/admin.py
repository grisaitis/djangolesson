'''
Created on Jul 24, 2011

@author: williamclaiborne
'''

'''
This admin script adds each model to the default admin site.
There are more things we could do here, which is why this is its own file, 
but we'll just do this for now. :)
'''

from django.contrib import admin
from djangolesson.members.models import Member, Study

admin.site.register( Member )
admin.site.register( Study )

