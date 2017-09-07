from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.

# is the unit test we’re writing be run by our automated test runner
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)