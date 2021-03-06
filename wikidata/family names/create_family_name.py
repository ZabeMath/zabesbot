import pywikibot
import sys
site = pywikibot.Site()
repo = site.data_repository()

name = sys.argv[1]

def create_item(repo, label_dict, desc_dict):
    new_item = pywikibot.ItemPage(repo)
    new_item.editLabels(labels=label_dict)
    new_item.editDescriptions(descriptions=desc_dict)
    # Add description here or in another function
    new_item.get()
    return new_item #new_item.getID()

new_item_labels = {
    "en": name,
    "de": name,
    "bar": name,
    "br": name,
    "ca": name,
    "co": name,
    "da": name,
    "de-at": name,
    "es": name,
    "fr": name,
    "id": name,
    "it": name,
    "nds": name,
    "nl": name,
    "no": name,
    "pl": name,
    "pt": name,
    "ro": name,
    "sl": name,
    "sv": name,
    "ty": name
}

new_item_desc = {
    'af': 'van',
    'an': 'apelliu',
    'ar': 'اسم العائلة',
    'ast': 'apellíu',
    'az': 'soyadı',
    'bar': 'Schreibnam',
    'be': 'прозвішча',
    'be-tarask': 'прозьвішча',
    'bg': 'презиме',
    'bn': 'পারিবারিক নাম',
    'br': 'anv-tiegezh',
    'bs': 'prezime',
    'ca': 'cognom',
    'crh': 'soyadı',
    'cs': 'příjmení',
    'csb': 'nôzwëskò',
    'cv': 'хушамат',
    'cy': 'cyfenw',
    'da': 'efternavn',
    'de': 'Familienname',
    'de-at': 'Familienname',
    'de-ch': 'Familienname',
    'el': 'επώνυμο',
    'en': 'family name',
    'en-ca': 'family name',
    'en-gb': 'surname',
    'eo': 'familia nomo',
    'es': 'apellido',
    'et': 'perekonnanimi',
    'eu': 'abizen',
    'fa': 'نام خانوادگی',
    'fi': 'sukunimi',
    'fit': 'sukunimi',
    'fo': 'ættarnavn',
    'fr': 'nom de famille',
    'fy': 'efternamme',
    'ga': 'sloinne',
    'gan': '姓氏箋釋',
    'gan-hans': '姓氏笺释',
    'gan-hant': '姓氏箋釋',
    'gd': 'sloinneadh',
    'gl': 'apelido',
    'gsw': 'Familiename',
    'gu': 'અટક',
    'gv': 'sliennoo',
    'he': 'שם משפחה',
    'hi': 'उपनाम',
    'hr': 'prezime',
    'hu': 'vezetéknév',
    'hy': 'ազգանուն',
    'id': 'nama keluarga',
    'ig': 'ahà nnà',
    'io': 'surnomo',
    'is': 'eftirnafn',
    'it': 'cognome',
    'ja': '姓',
    'jut': 'efternavn',
    'jv': 'jeneng pancer',
    'ka': 'გვარი',
    'kk': 'тек, ата-тек, әулет есім',
    'kk-cyrl': 'тек, ата-тек, әулет есім',
    'kk-latn': 'tek, ata-tek, äwlet esim',
    'kk-kz': 'тек, ата-тек, әулет есім',
    'kk-tr': 'tek, ata-tek, äwlet esim',
    'ko': '성씨',
    'ksh': 'Nohnahme',
    'kw': 'hanow',
    'la': 'nomen gentilicium',
    'lad': 'alkunya',
    'lb': 'Familljennumm',
    'lt': 'pavardė',
    'lv': 'uzvārds',
    'lzh': '姓氏',
    'mhr': 'тукымлӱм',
    'mi': 'ingoa whānau',
    'min': 'namo asli',
    'mk': 'презиме',
    'mn': 'овог нэр',
    'ms': 'nama keluarga',
    'mt': 'kunjom',
    'nb': 'etternavn',
    'nds': 'Familiennaam',
    'ne': 'थर',
    'new': 'उपनां',
    'nl': 'achternaam',
    'nn': 'etternamn',
    'oc': 'nom d’ostal',
    'or': 'ସାଙ୍ଗିଆ',
    'os': 'мыггаг',
    'pl': 'nazwisko',
    'pms': 'cognòm',
    'pt': 'sobrenome',
    'pt-br': 'nome de familia',
    'ro': 'nume de familie',
    'ru': 'фамилия',
    'rue': 'прузвище',
    'sco': 'faimily name',
    'se': 'goargu',
    'sh': 'prezime',
    'sje': 'maŋŋepnamma',
    'sk': 'priezvisko',
    'sl': 'priimek',
    'sma': 'fuelhkienomme',
    'smj': 'maŋepnamma',
    'sn': 'Mazita eMhuri',
    'sq': 'mbiemër',
    'sr': 'презиме',
    'sr-ec': 'презиме',
    'sr-el': 'prezime',
    'sv': 'efternamn',
    'sw': 'jina la ukoo',
    'ta': 'குடும்பப் பெயர்',
    'te': 'ఇంటి పేర్లు',
    'tg': 'насаб',
    'tg-cyrl': 'насаб',
    'tg-latn': 'nasab',
    'th': 'นามสกุล',
    'tl': 'apelyido',
    'tr': 'soyadı',
    'uk': 'прізвище',
    'uz': 'familiya',
    'vi': 'họ',
    'wa': 'no d’ famile',
    'war': 'apelyidu',
    'xh': 'ifani',
    'yi': 'פֿאַמיליע נאָמען',
    'yue': '姓',
    'zh': '姓氏',
    'zh-cn': '姓氏',
    'zh-hans': '姓氏',
    'zh-hant': '姓氏',
    'zh-hk': '姓氏',
    'zh-mo': '姓氏',
    'zh-my': '姓氏',
    'zh-sg': '姓氏',
    'zh-tw': '姓氏',
    'zu': 'isibongo'
}

item = create_item(repo, new_item_labels, new_item_desc)
claim = pywikibot.Claim(repo, u'P31')
family_name = pywikibot.ItemPage(repo, "Q101352")
claim.setTarget(family_name)
item.addClaim(claim)
claim2 = pywikibot.Claim(repo, u'P282')
latin_script = pywikibot.ItemPage(repo, "Q8229")
claim2.setTarget(latin_script)
item.addClaim(claim2)

if len(sys.argv) > 2:
    criterion = pywikibot.Claim(repo, u'P1013')
    different = pywikibot.ItemPage(repo, "Q27924673")
    criterion.setTarget(different)
    dis = pywikibot.ItemPage(repo,sys.argv[2])
    claim3 = pywikibot.Claim(repo, u'P1889')
    claim3.setTarget(dis)
    claim3.addQualifier(criterion)
    item.addClaim(claim3)
    criterion2 = pywikibot.Claim(repo, u'P1013')
    different2 = pywikibot.ItemPage(repo, "Q27924673")
    criterion2.setTarget(different2)
    claim4 = pywikibot.Claim(repo, u'P1889')
    claim4.setTarget(item)
    claim4.addQualifier(criterion2)
    dis.addClaim(claim4)
