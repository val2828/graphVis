from django.test import TestCase
from django.urls import resolve
from graphs.views import home_page

from django.test import LiveServerTestCase
from selenium import webdriver
import time
# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

class VisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        time.sleep(10)
        self.browser.quit()

    def test_can_see_title_and_header(self):
        self.browser.get('http://localhost:8080')
        
        self.assertIn('Basic Graph',self.browser.title)