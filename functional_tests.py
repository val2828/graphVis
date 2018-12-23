from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
# Create your tests here.

class VisitHomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        

    def tearDown(self):
        self.browser.quit()

    def test_user_sees_the_title(self):
        # visit the page
        self.browser.get('http://localhost:8080')

        # check if the title is correct 
        self.assertIn('Basic Graph',self.browser.title)
        header_text = self.browser.find_element_by_id('header').text
        self.assertIn('Graph', header_text)  

        self.fail('Finished tests!')      

if __name__ == '__main__':
    unittest.main(warnings='ignore')