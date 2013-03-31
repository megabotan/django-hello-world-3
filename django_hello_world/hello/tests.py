from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from hello.models import Person
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver


class HttpTest(TestCase):
    def setUp(self):
        self.me = Person.objects.get(id=1)

    def test_home(self):
        c = Client()
        response = c.get('/')
        self.assertContains(response,self.me.name)
        self.assertContains(response,self.me.bio)
        self.assertContains(response,self.me.email)




class HttpTestSelenium(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        super(HttpTestSelenium, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HttpTestSelenium, cls).tearDownClass()
        cls.driver.quit()
    

    def test_home(self):
        self.driver.get(self.live_server_url)
        body = self.driver.find_element_by_tag_name('body')

        self.assertIn(self.me.name, body.text)
        self.assertIn(self.me.bio, body.text)
        self.assertIn(self.me.email, body.text)

    
    def test_check_admin_work_and_contains_Person(self):
        self.driver.get(self.live_server_url + '/admin/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)#checks admin is up

        username_field = self.driver.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)#checks you can login

        polls_links = self.driver.find_elements_by_link_text('Person')
        self.assertEquals(len(polls_links), 2)#checks that Person is added to admin

       

