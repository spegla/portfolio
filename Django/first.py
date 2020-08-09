from django.http import HttpResponse
import datetime

def current_time(request):
    now = datetime.datetime.now()
    hmtl ="<hmtl><body>The time | is now %s.</body></hmtl>" % now
    return httpresponse
