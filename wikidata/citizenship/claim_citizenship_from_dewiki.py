import sys
import pywikibot
from pywikibot import pagegenerators

def is_human(repository, item):
    if item.claims:
        if 'P31' in item.claims:
            for claim in item.claims['P31']:
                if cliam.getTarget() == pywikibot.ItemPage(repository, "Q5"):
                    return True
    return False

site = pywikibot.Site()
repo = site.data_repository()
category = sys.argv[1]
country = pywikibot.ItemPage(repo,sys.argv[2])
cat = pywikibot.Category(site,category)
gen = pagegenerators.CategorizedPageGenerator(cat)
for page in gen:
    item = pywikibot.ItemPage.fromPage(page)
    print(item)
    b_create = True
    if item.claims:
        if 'P27' in item.claims:
            for subclaim in item.claims['P27']:
                if subclaim.getTarget() == country:
                    b_create = False
    if b_create and is_human(repo, item):
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
