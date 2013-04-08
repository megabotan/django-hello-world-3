from django_hello_world.hello.models import Person, Request
from django_hello_world.hello.forms import PersonForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
import os


def home(request):
    person = get_object_or_404(Person, id=settings.MY_ID)
    return render(request, 'hello/index.html', {'person': person})


def requests(request):
    first_requests = Request.objects.all().order_by('date')[:10]
    return render(request, 'hello/requests.html',
                  {'first_requests': first_requests})


@login_required
def edit(request):
    person = get_object_or_404(Person, id=settings.MY_ID)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form = PersonForm(request.POST, request.FILES, instance=person)
            clear_images_folder()
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PersonForm(instance=person)
    return render(request, 'hello/edit.html', {
        'form': form,
        'person': person
    })


def clear_images_folder():
    folder = os.path.join(os.path.dirname(__file__), 'static/media/images')
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path) and the_file != 'default.jpg':
                os.unlink(file_path)
        except Exception, e:
            print e
