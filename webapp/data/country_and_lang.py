import json
import os

country_isocodesline = "aearataubebgbrcachcncocuczdeegfrgbgrhkhuidieilinitjpkrltlvmamxmyngnlnonzphplptrorsrusasesgsiskthtrtwuausveza"  # 2 character country codes

lang_isocodesline = "ardeenesfrheitnlnoptruseudzh"  # 2 character language codes


def isocodesline_to_list(line):
    return [line[i: i + 2] for i in range(0, len(line), 2)]


def get_country_list():
    countrycode_list = isocodesline_to_list(country_isocodesline)
    world_countries = json.load(open(os.path.join(os.path.dirname(__file__), 'world_country_list.json')))
    country_list = filter(lambda e: e['Code'].lower() in countrycode_list, world_countries)
    country_list = [{'code': e['Code'], 'name': e['Name']} for e in country_list]
    return country_list


def get_lang_list():
    return isocodesline_to_list(lang_isocodesline)
