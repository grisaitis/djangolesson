from django.http import HttpResponse
from models import Member
from django.shortcuts import render_to_response
from djangolesson.members.forms import NameForm

# Create your views here.

''' 
What's a `view`?

"... A view is a simple python function that takes at least one variable, 
the request context, which contains some extra data like the URL, form 
input, logged in user, etc. The view should always return an HTTP 
compatible message. The easiest way is to use HttpResponse, which just 
sends some text back that will be displayed in the browser."
    - from djangoles-tutorial.pdf, pg. 3
'''

def myFirstView( request ):
    return HttpResponse( "Hey William :)" )

def membersList( request ):
    result = ""
    for m in Member.objects.all():
#        result += "%s" % m.first_name
        result += "%s --- study: %s<br />" % ( m, m.study )
#    result = "test"
    return HttpResponse( result )

def betterMembersList( request ):
    variables = { "members" : Member.objects.all() }
    return render_to_response( "members/list.html", variables )

def formView( request ):
    f = NameForm( request.GET )
    if f.is_valid():
        return render_to_response( "members/welcome.html", {"name": f.getName()} )
    return render_to_response( "members/form.html", {"form": f} )
