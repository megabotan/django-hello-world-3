"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from hello.models import Person


class HelloTest(TestCase):

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class HttpTest(TestCase):
    def setUp(self):
        self.me = Person.objects.get(id=1)

    def test_home(self):
        c = Client()
        response = c.get('/')
        self.assertContains(response,self.me.name)
        self.assertContains(response,self.me.date_of_birth)
        self.assertContains(response,self.me.bio)
        self.assertContains(response,self.me.contacts)


