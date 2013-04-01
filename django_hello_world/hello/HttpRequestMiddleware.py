from django_hello_world.hello.models import Request
from django.utils import timezone


class Middleware:
    def process_request(self, request):
        r = Request(path=request.path, method=request.method,
                    user=request.user, date=timezone.now())
        r.save()
