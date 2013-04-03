from django.test import TestCase
from django_hello_world.hello.models import Person, Request
from django.conf import settings


class HttpTest(TestCase):
    def setUp(self):
        self.me = Person.objects.get(id=settings.MY_ID)

    def test_home(self):
        response = self.client.get('/')
        self.assertContains(response, self.me.name)
        for string in self.me.bio.splitlines():
            self.assertContains(response, string)
        self.assertContains(response, self.me.email)

    def test_requests(self):
        requestString = '/vblkzlcxvbru'
        self.client.get(requestString)
        response = self.client.get('/requests/')
        for req in Request.objects.all().order_by('date')[:10]:
            self.assertContains(response, req.path)


class MiddlewareTest(TestCase):
    def test(self):
        requestString = '/vblkzlcxvbru'
        self.client.get(requestString)
        lastRequest = Request.objects.get(path=requestString)
        self.assertEquals(lastRequest.method, "GET")


class TemplateContextProcessor(TestCase):
    def test_settings(self):
        requestString = '/vblkzlcxvbru'
        response = self.client.get(requestString)
        self.assertTrue('settings' in response.context)
        self.assertEquals(response.context['settings'], settings)
