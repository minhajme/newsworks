from unittest import TestCase
import pprint
from django.test import TestCase as DjangoTestCase
from webapp.data.country_and_lang import get_country_names
from webapp.forms import NewsSettingsForm


class CountryCodeNameTest(TestCase):
    def test_countrycodetoname(self):
        country_list = get_country_names()
        self.assertNotEqual(len(country_list), 0)


country_input_data1 = 'ae,ar,at,au,be'
country_input_data2 = 'ae,ar,at,au,bd'
source_input_data1 = 'abc-news, abc-news-au'
keywords_input_data1 = 'abc-news, bbc'


class NewsSettingsFormTest(TestCase):
    def test_1(self):
        form = NewsSettingsForm(
            {'country': country_input_data1, 'source': source_input_data1, 'keywords': keywords_input_data1})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.cleaned_data['country'].split(',')), 5)
        self.assertEqual(len(form.cleaned_data['source'].split(',')), 2)

    def test2(self):
        form = NewsSettingsForm(
            {'country': country_input_data2})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['country'], 'ae,ar,at,au')
