# Create your views here.
from django.http import HttpResponse

def printWelcome( request ):
    return HttpResponse( "Hello, world! This is a test homepage for the basic URL." )
