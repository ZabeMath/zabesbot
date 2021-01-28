import sys
import pywikibot
from pywikibot import pagegenerators
site = pywikibot.Site()
repo = site.data_repository()
category = sys.argv[1]
country = pywikibot.ItemPage(repo,sys.argv[2])
cat = pywikibot.Category(site,category)
gen = pagegenerators.CategorizedPageGenerator(cat)
for page in gen:
    item = pywikibot.ItemPage.fromPage(page)
    print(item)
    b_create = False
    if item.claims:
        if 'P31' in item.claims:
            for subclaim in item.claims['P31']:
                if subclaim.getTarget() == pywikibot.ItemPage(repo, "Q5"):
                    b_create = True
        if 'P27' in item.claims:
            for subclaim in item.claims['P27']:
                if subclaim.getTarget() == country:
                    b_create = False
    if b_create:
        print("create claim")
        claim = pywikibot.Claim(repo, u'P27')
        claim.setTarget(country)
        importedfrom = pywikibot.Claim(repo, u'P143')
        dewiki = pywikibot.ItemPage(repo, "Q48183")
        importedfrom.setTarget(dewiki)
        heuristic = pywikibot.Claim(repo, u'P887')
        from_cat = pywikibot.ItemPage(repo, u'Q87206960')
        heuristic.setTarget(from_cat)
        claim.addSources([importedfrom, heuristic])
        item.addClaim(claim)
