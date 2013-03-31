from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from hello.models import Person
from django.conf import settings


class HelloTest(TestCase):

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

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

