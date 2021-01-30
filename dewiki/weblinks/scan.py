import pywikibot
from pywikibot import pagegenerators
site = pywikibot.Site()
repo = site.data_repository()
gen = pagegenerators.SearchPageGenerator("insource:/bundeswehr.de/",site=site)
out = "=== bundeswehr.de ===\n"
for page in gen:
    try:
        item = pywikibot.ItemPage.fromPage(page)
        item.get()
        out = out + "# [[" + str(item.getSitelink(site)) + "]]\n"
        print(str(item.getSitelink(site)))
    except:
        pass

dest = pywikibot.Page(site, u"Benutzer:LW-Pio/Bundeswehrlinks")
text = dest.text
text = text + out
dest.text = text
dest.save("Bot: Linkscan")

gen = pagegenerators.SearchPageGenerator("insource:/deutschesheer.de/",site=site)
out = "=== deutschesheer.de ===\n"
for page in gen:
    try:
        item = pywikibot.ItemPage.fromPage(page)
        item.get()
        out = out + "# [[" + str(item.getSitelink(site)) + "]]\n"
        print(str(item.getSitelink(site)))
    except:
        pass

dest = pywikibot.Page(site, u"Benutzer:LW-Pio/Bundeswehrlinks")
text = dest.text
text = text + out
dest.text = text
dest.save("Bot: Linkscan")

gen = pagegenerators.SearchPageGenerator("insource:/luftwaffe.de/",site=site)
out = "=== luftwaffe.de ===\n"
for page in gen:
    try:
        item = pywikibot.ItemPage.fromPage(page)
        item.get()
        out = out + "# [[" + str(item.getSitelink(site)) + "]]\n"
        print(str(item.getSitelink(site)))
    except:
        pass

dest = pywikibot.Page(site, u"Benutzer:LW-Pio/Bundeswehrlinks")
text = dest.text
text = text + out
dest.text = text
dest.save("Bot: Linkscan")

gen = pagegenerators.SearchPageGenerator("insource:/marine.de/",site=site)
out = "=== marine.de ===\n"
for page in gen:
    try:
        item = pywikibot.ItemPage.fromPage(page)
        item.get()
        out = out + "# [[" + str(item.getSitelink(site)) + "]]\n"
        print(str(item.getSitelink(site)))
    except:
        pass

dest = pywikibot.Page(site, u"Benutzer:LW-Pio/Bundeswehrlinks")
text = dest.text
text = text + out
dest.text = text
dest.save("Bot: Linkscan")

gen = pagegenerators.SearchPageGenerator("insource:/sanitaetsdienst-bundeswehr.de/",site=site)
out = "=== sanitaetsdienst-bundeswehr.de ===\n"
for page in gen:
    try:
        item = pywikibot.ItemPage.fromPage(page)
        item.get()
        out = out + "# [[" + str(item.getSitelink(site)) + "]]\n"
        print(str(item.getSitelink(site)))
    except:
        pass

dest = pywikibot.Page(site, u"Benutzer:LW-Pio/Bundeswehrlinks")
text = dest.text
text = text + out
dest.text = text
dest.save("Bot: Linkscan")

gen = pagegenerators.SearchPageGenerator("insource:/streitkraeftebasis.de/",site=site)
out = "=== streitkraeftebasis.de ===\n"
for page in gen:
    try:
        item = pywikibot.ItemPage.fromPage(page)
        item.get()
        out = out + "# [[" + str(item.getSitelink(site)) + "]]\n"
        print(str(item.getSitelink(site)))
    except:
        pass

dest = pywikibot.Page(site, u"Benutzer:LW-Pio/Bundeswehrlinks")
text = dest.text
text = text + out
dest.text = text
dest.save("Bot: Linkscan")

gen = pagegenerators.SearchPageGenerator("insource:/zmsbw.de/",site=site)
out = "=== zmsbw.de ===\n"
for page in gen:
    try:
        item = pywikibot.ItemPage.fromPage(page)
        item.get()
        out = out + "# [[" + str(item.getSitelink(site)) + "]]\n"
        print(str(item.getSitelink(site)))
    except:
        pass

dest = pywikibot.Page(site, u"Benutzer:LW-Pio/Bundeswehrlinks")
text = dest.text
text = text + out
dest.text = text
dest.save("Bot: Linkscan")
