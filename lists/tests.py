from django.test import TestCase

# Create your tests here.

# is the unit test we’re writing be run by our automated test runner
class SmokeTest(TestCase):
    
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)