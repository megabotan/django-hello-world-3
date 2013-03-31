from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from hello.models import Person
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.me = Person.objects.get(id=1)

    def tearDown(self):
        self.browser.quit()
    

    def test_home(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element_by_tag_name('body')

        self.assertIn(self.me.name, body.text)
        self.assertIn(self.me.bio, body.text)
        self.assertIn(self.me.email, body.text)

    
    def test_check_admin_work_and_contains_Person(self):
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)#checks admin is up

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)#checks you can login

        polls_links = self.browser.find_elements_by_link_text('Person')
        self.assertEquals(len(polls_links), 2)#checks that Person is added to admin

       

