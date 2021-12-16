from django.test import TestCase
from webapp.data.country_and_lang import get_country_list


# Create your tests here.

class CountryCodeNameTest(TestCase):
    def test_countrycodetoname(self):
        country_list = get_country_list()
        self.assertNotEqual(len(country_list), 0)
