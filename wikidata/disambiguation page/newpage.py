import re
import urllib
import pywikibot
from pywikibot import pagegenerators

def create_item(repo, name):
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
        'an': 'pachina de desambigación de Wikimedia',
        'ar': 'صفحة توضيح لويكيميديا',
        'be': 'старонка неадназначнасці ў праекце Вікімедыя',
        'bg': 'Уикимедия пояснителна страница',
        'bn': 'উইকিমিডিয়ার দ্ব্যর্থতা নিরসন পাতা',
        'bs': 'čvor stranica na Wikimediji',
        'ca': 'pàgina de desambiguació de Wikimedia',
        'ckb': 'پەڕەی ڕوونکردنەوەی ویکیمیدیا',
        'cs': 'rozcestník na projektech Wikimedia',
        'da': 'Wikimedia-flertydigside',
        'de': 'Wikimedia-Begriffsklärungsseite',
        'de-at': 'Wikimedia-Begriffsklärungsseite',
        'de-ch': 'Wikimedia-Begriffsklärungsseite',
        'el': 'σελίδα αποσαφήνισης εγχειρημάτων Wikimedia',
        'en': 'Wikimedia disambiguation page',
        'en-ca': 'Wikimedia disambiguation page',
        'en-gb': 'Wikimedia disambiguation page',
        'eo': 'Vikimedia apartigilo',
        'es': 'página de desambiguación de Wikimedia',
        'et': 'Wikimedia täpsustuslehekülg',
        'eu': 'Wikimediako argipen orri',
        'fa': 'یک صفحهٔ ابهام\u200cزدایی در ویکی\u200cپدیا',
        'fi': 'Wikimedia-täsmennyssivu',
        'fr': 'page d\'homonymie de Wikimedia',
        'fy': 'Wikimedia-betsjuttingsside',
        'gl': 'páxina de homónimos de Wikimedia',
        'gsw': 'Wikimedia-Begriffsklärigssite',
        'gu': 'સ્પષ્ટતા પાનું',
        'he': 'דף פירושונים',
        'hi': 'बहुविकल्पी पृष्ठ',
        'hr': 'razdvojbena stranica na Wikimediji',
        'hu': 'Wikimédia-egyértelműsítőlap',
        'hy': 'Վիքիմեդիայի նախագծի բազմիմաստության փարատման էջ',
        'id': 'halaman disambiguasi',
        'is': 'aðgreiningarsíða á Wikipediu',
        'it': 'pagina di disambiguazione di un progetto Wikimedia',
        'ja': 'ウィキメディアの曖昧さ回避ページ',
        'ka': 'მრავალმნიშვნელოვანი',
        'ko': '위키미디어 동음이의어 문서',
        'lb': 'Wikimedia-Homonymiesäit',
        'li': 'Wikimedia-verdudelikingspazjena',
        'lv': 'Wikimedia projekta nozīmju atdalīšanas lapa',
        'min': 'laman disambiguasi',
        'mk': 'појаснителна страница на Викимедија',
        'ms': 'laman nyahkekaburan',
        'nb': 'Wikimedia-pekerside',
        'nds': 'Sied för en mehrdüdig Begreep op Wikimedia',
        'nl': 'Wikimedia-doorverwijspagina',
        'nn': 'Wikimedia-fleirtydingsside',
        'or': 'ବହୁବିକଳ୍ପ ପୃଷ୍ଠା',
        'pl': 'strona ujednoznaczniająca w projekcie Wikimedia',
        'pt': 'página de desambiguação da Wikimedia',
        'pt-br': 'página de desambiguação da Wikimedia',
        'ro': 'pagină de dezambiguizare Wikimedia',
        'ru': 'страница значений в проекте Викимедиа',
        'sco': 'Wikimedia disambiguation page',
        'sk': 'rozlišovacia stránka projektov Wikimedia',
        'sl': 'razločitvena stran Wikimedije',
        'sq': 'faqe kthjelluese e Wikimedias',
        'sr': 'вишезначна одредница на Викимедији',
        'sv': 'Wikimedia-förgreningssida',
        'sw': 'ukarasa wa maana wa Wikimedia',
        'tg': 'саҳифаи маъноҳои Викимедиа',
        'tg-cyrl': 'саҳифаи маъноҳои Викимедиа',
        'tg-latn': 'sahifai ma\'nohoi Vikimedia',
        'tr': 'Wikimedia anlam ayrımı sayfası',
        'tt': 'Мәгънәләр бите Викимедиа проектында',
        'tt-cyrl': 'Мәгънәләр бите Викимедиа проектында',
        'tt-latn': 'Mäğnälär bite Wikimedia proyektında',
        'uk': 'сторінка значень у проекті Вікімедіа',
        'vi': 'trang định hướng Wikimedia',
        'yi': 'וויקימעדיע באַדייטן בלאַט',
        'yo': 'ojúewé ìṣojútùú Wikimedia',
        'yue': '維基媒體搞清楚頁',
        'zea': 'Wikimedia-deurverwiespagina',
        'zh': '维基媒体消歧义页',
        'zh-cn': '维基媒体消歧义页',
        'zh-hans': '维基媒体消歧义页',
        'zh-hant': '維基媒體消歧義頁',
        'zh-hk': '維基媒體消歧義頁',
        'zh-mo': '維基媒體消歧義頁',
        'zh-my': '维基媒体消歧义页',
        'zh-sg': '维基媒体消歧义页',
        'zh-tw': '維基媒體消歧義頁'
    }
    new_item = pywikibot.ItemPage(repo)
    new_item.editLabels(labels=label_dict)
    new_item.editDescriptions(descriptions=new_item_desc)
    new_item.get()
    return new_item #new_item.getID()

def pageIsDisambiguationPage(page):
    return re.search(r'(?im)({{Begriffsklärung}})', page.text)

def getURL(url='', retry=True, timeout=30):
    raw = ''
    req = urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0' })
    try:
        raw = urllib.request.urlopen(req, timeout=timeout).read().strip().decode('utf-8')
    except:
        sleep = 10 # seconds
        maxsleep = 900
        while retry and sleep <= maxsleep:
            print('Error while retrieving: %s' % (url))
            print('Retry in %s seconds...' % (sleep))
            time.sleep(sleep)
            try:
                raw = urllib.request.urlopen(req, timeout=timeout).read().strip().decode('utf-8')
            except:
                pass
            sleep = sleep * 2
    return raw

site = pywikibot.Site(fam='wikipedia', code='de')
sitewd = pywikibot.Site(fam='wikidata', code='wikidata')
repo = site.data_repository()
repowd = sitewd.data_repository()
total = 20
lang = 'de'
gen = pagegenerators.NewpagesPageGenerator(site=site, namespaces=[0], total=total)
pre = pagegenerators.PreloadingGenerator(gen, groupsize=total)
for page in pre:
    item = ''
    try:
        item = pywikibot.ItemPage.fromPage(page)
    except:
        pass
    if item:
        print('Page has item')
    else:
        if not pageIsDisambiguationPage(page):
            print('Page is not disambiguation page')
        else:
            print(page.title())
            wtitle = page.title()
            wtitle_ = wtitle.split('(')[0].strip()
            searchitemurl = 'https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=%s&format=xml' % (urllib.parse.quote(wtitle_), lang)
            raw = getURL(searchitemurl)
            m = re.findall(r'id="(Q\d+)"', raw)
            if len(m) == 0:
                new_item = create_item(repo, wtitle)
                new_item.setSitelink(page)
            #for itemfoundq in m:
            #    item = ''
            #    try:
            #        item = pywikibot.ItemPage(repo,itemfoundq)
            #    except:
            #        pass
            #    if item:
            #        print(item)
