country_isocodesline = "aearataubebgbrcachcncocuczdeegfrgbgrhkhuidieilinitjpkrltlvmamxmyngnlnonzphplptrorsrusasesgsiskthtrtwuausveza"  # 2 character country codes

lang_isocodesline = "ardeenesfrheitnlnoptruseudzh"  # 2 character language codes


def isocodesline_to_list(line):
    return [line[i: i + 2] for i in range(0, len(line), 2)]


def country_list():
    return isocodesline_to_list(country_isocodesline)


def lang_list():
    return isocodesline_to_list(lang_isocodesline)
