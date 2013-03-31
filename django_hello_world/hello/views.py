from django.contrib.auth.models import User
from hello.models import Person
from django.shortcuts import render, get_object_or_404

def home(request):
    person = get_object_or_404(Person, id=1)
    return render(request, "hello/index.html", {"person": person})



