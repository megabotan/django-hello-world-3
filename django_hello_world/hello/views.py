from django.contrib.auth.models import User
from hello.models import Person
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

def home(request):
    try:
        person = Person.objects.get(id=1)
    except Person.DoesNotExist:
        raise Http404    
    #person = get_object_or_404(Person, id=1)
    return render_to_response("hello/index.html", {"person": person})



