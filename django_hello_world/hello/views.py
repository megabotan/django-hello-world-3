from django.contrib.auth.models import User
from django_hello_world.hello.models import Person
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext

def home(request):
    try:
        person = Person.objects.get(id=1)
    except Person.DoesNotExist:
        raise Http404    
    return render_to_response("hello/index.html", {"person": person}, RequestContext(request))



