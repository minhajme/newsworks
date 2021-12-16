# populate news source and country db

import djangoinit
from django.conf import settings
import requests
import pprint

from webapp.data.country_and_lang import country_list, get_lang_list
from webapp.models import NewsSource

response = requests.get(f"https://newsapi.org/v2/top-headlines/sources?apiKey={settings.NEWSAPIKEY}")

if response.status_code != 200:
    raise Exception('Request did not succeed')

response_json = response.json()

if response_json['status'] != "ok":
    raise Exception("Response not usable")

for source in response_json['sources']:
    pprint.pprint(source)
    NewsSource(**{key.name: source[key.name] for key in NewsSource._meta.get_fields()}).save()
    print('*****SAVED*****')

print(str(len(response_json['sources'])) + ' sources')
