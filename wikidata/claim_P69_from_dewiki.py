import sys
import pywikibot
from pywikibot import pagegenerators
site = pywikibot.Site()
repo = site.data_repository()
category = sys.argv[1]
uni = pywikibot.ItemPage(repo,sys.argv[2])
not_claim_when_claimed = [uni]
if uni.claims:
    if 'P355' in uni.claims:
        for subclaim in uni.claims['P355']:
            not_claim_when_claimed.append(subclaim.getTarget())
    if 'P527' in uni.claims:
        for subclaim in uni.claims['P527']:
            not_claim_when_claimed.append(subclaim.getTarget())
cat = pywikibot.Category(site,category)
gen = pagegenerators.CategorizedPageGenerator(cat)
for page in gen:
    item = pywikibot.ItemPage.fromPage(page)
    b_claim = True
    if item.claims:
        if 'P69' in item.claims:
            for claim in item.claims['P69']:
                target = claim.getTarget()
                for no in not_claim_when_claimed:
                    if target == no:
                        b_claim = False
    if b_claim:
        claim = pywikibot.Claim(repo, u'P69')
        claim.setTarget(uni)
        importedfrom = pywikibot.Claim(repo, u'P143')
        dewiki = pywikibot.ItemPage(repo, "Q48183")
        importedfrom.setTarget(dewiki)
        claim.addSources([importedfrom])
        item.addClaim(claim)
