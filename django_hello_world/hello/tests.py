"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django_hello_world.hello.models import Person, Request
from django.conf import settings

class HttpTest(TestCase):
    def setUp(self):
        self.me = Person.objects.get(id=settings.MY_ID)

    def test_home(self):
        c = Client()
        response = c.get('/')
        self.assertContains(response,self.me.name)
        for string in self.me.bio.splitlines():
            self.assertContains(response,string)
        self.assertContains(response,self.me.email)

class MiddlewareTest(TestCase):
    def test(self):
        requestString='/vblkzlcxvbru'
        c = Client()
        c.get(requestString)
        lastRequest = Request.objects.get(path=requestString)#if something is wrong will throw exception
        self.assertTrue(True)
        
        
