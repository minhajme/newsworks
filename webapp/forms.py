from django import forms
from webapp.data.country_and_lang import get_country_list
from webapp.models import NewsSource
from .helpers import list_strip


class NewsSettingsForm(forms.Form):
    country = forms.CharField(required=False)  # comma separated values. ISO 2 char codes.
    source = forms.CharField(required=False)  # comma separated values. news source ids
    keywords = forms.CharField(required=False)  # comma separated strings

    def clean_country(self):
        checked_country_list = list_strip(self.cleaned_data.get('country', '').split(','))
        available_country_list = get_country_list()
        cleaned_list = list(filter(lambda e: e in available_country_list, checked_country_list))
        return ','.join(cleaned_list)

    def clean_source(self):
        checked_source_list = list_strip(self.cleaned_data.get('source', '').split(','))
        available_source_list = [s['id'] for s in NewsSource.objects.all().values('id')]
        return ','.join(list(filter(lambda e: e in available_source_list, checked_source_list)))
