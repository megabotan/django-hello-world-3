from django_hello_world.hello.models import Person, Request
from django_hello_world.hello.forms import PersonForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.conf import settings


def home(request):
    person = get_object_or_404(Person, id=settings.MY_ID)
    return render(request, 'hello/index.html', {'person': person})


def requests(request):
    first_requests = Request.objects.all().order_by('date')[:10]
    return render(request, 'hello/requests.html',
                  {'first_requests': first_requests})


def edit(request):
    person = get_object_or_404(Person, id=settings.MY_ID)
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form = PersonForm(request.POST, instance=person)
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PersonForm(instance=person)
    return render(request, 'hello/edit.html', {
        'form': form,
        'person': person
    })
