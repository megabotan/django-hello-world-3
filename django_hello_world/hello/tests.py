from django.test import TestCase
from django.test.client import Client
from django_hello_world.hello.models import Person
from django.conf import settings
from django.test import LiveServerTestCase
import unittest


def selenium_not_exists():
    try:
        __import__('selenium')
    except ImportError:
        return True
    else:
        return False


class HttpTest(TestCase):
    def setUp(self):
        self.me = Person.objects.get(id=settings.MY_ID)

    def test_home(self):
        c = Client()
        response = c.get('/')
        self.assertContains(response, self.me.name)
        for string in self.me.bio.splitlines():
            self.assertContains(response, string)
        self.assertContains(response, self.me.email)


@unittest.skipIf(selenium_not_exists(), "selenium cant work in virtualenv")
class HttpTestSelenium(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        from selenium.webdriver.firefox.webdriver import WebDriver
        cls.driver = WebDriver()
        super(HttpTestSelenium, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HttpTestSelenium, cls).tearDownClass()
        cls.driver.quit()

    def test_check_admin_work_and_contains_Person(self):
        from selenium.webdriver.common.keys import Keys
        self.driver.get(self.live_server_url + '/admin/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)  # checks admin is up

        username_field = self.driver.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)  # checks you can login

        polls_links = self.driver.find_elements_by_link_text('Persons')
        self.assertEquals(len(polls_links), 1)  # checks Person in admin
