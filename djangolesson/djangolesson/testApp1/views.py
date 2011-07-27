# Create your views here.

from django.http import HttpResponse

def testApp1_view1( request ):
    return HttpResponse( "My name is William Claiborne Grisaitis. \nThis is my first web site of a few awesome ones made with Django.\nBack to work!! :)" )
