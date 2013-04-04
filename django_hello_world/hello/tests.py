from django.test import TestCase
from django_hello_world.hello.models import Person, Request
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
        response = self.client.get('/')
        self.assertContains(response, self.me.name)
        for string in self.me.bio.splitlines():
            self.assertContains(response, string)
        self.assertContains(response, self.me.email)

    def test_requests(self):
        reqests_on_page = settings.REQUESTS_ON_PAGE
        for i in range(reqests_on_page*2):
            requestString = '/vblkzlcxvbru' + str(i)
            self.client.get(requestString)
        response = self.client.get('/requests/')
        expected_requests = (Request.objects.all()
                             .order_by('date')[:reqests_on_page*2]
                             )
        for i in range(reqests_on_page):
            self.assertContains(response, expected_requests[i].path)
        for i in range(reqests_on_page, reqests_on_page*2):
            self.assertNotContains(response, expected_requests[i].path)


@unittest.skipIf(selenium_not_exists(), "selenium cant work in virtualenv")
class HttpTestSelenium(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        from selenium.webdriver.firefox.webdriver import WebDriver
        cls.driver = WebDriver()
        super(HttpTestSelenium, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(HttpTestSelenium, cls).tearDownClass()

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

    def test_requests_page(self):
        reqests_on_page = settings.REQUESTS_ON_PAGE
        for i in range(reqests_on_page*2):
            requestString = '/vblkzlcxvbru' + str(i)
            self.driver.get(self.live_server_url + requestString)
        self.driver.get(self.live_server_url + '/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('requests', body.text)  # checks requests href
        self.driver.find_element_by_link_text("requests").click()
        body = self.driver.find_element_by_tag_name('body')
        expected_requests = (Request.objects.all()
                             .order_by('date')[:reqests_on_page*2]
                             )
        for i in range(reqests_on_page):
            self.assertIn(expected_requests[i].path, body.text)
        for i in range(reqests_on_page, reqests_on_page*2):
            self.assertNotIn(expected_requests[i].path, body.text)
