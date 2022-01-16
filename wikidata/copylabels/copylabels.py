import pywikibot
from pywikibot import pagegenerators

maximum = 10000
stepsize =  10000
numsteps = int(maximum / stepsize)

site = pywikibot.Site("wikidata", "wikidata")

for i in range(numsteps):
    query = "SELECT ?item\n"\
    "WITH { \n"\
    "  SELECT ?item WHERE {\n"\
    "    ?item wdt:P31 wd:Q5 . \n"\
    '  } LIMIT ' + str(stepsize) + ' OFFSET ' + str(i*stepsize) + '\n'\
    "} AS %items\n"\
    "WHERE {\n"\
    "  INCLUDE %items .\n"\
    "    SERVICE wikibase:label { bd:serviceParam wikibase:language \"de\". }\n"\
    "    FILTER(NOT EXISTS {\n"\
    "        ?item rdfs:label ?lang_label.\n"\
    "        FILTER(LANG(?lang_label) in ('de-formal'))\n"\
    "    })\n"\
    "    FILTER(EXISTS {\n"\
    "        ?item rdfs:label ?lang_label.\n"\
    "        FILTER(LANG(?lang_label) in ('de'))\n"\
    "    })\n"\
    "}"

    print(query)

    generator = pagegenerators.WikidataSPARQLPageGenerator(query, site=site)
    for page in generator:
        try:
            item = page.get()
            label = item['labels']['de']
            qid = page.title()
        except:
            continue

        print(f'Processing {qid}.')

        if label != '':
            new_labels = {'de-formal': label}
            for lang in ['de-at', 'de-ch']:
                if lang not in item['labels']:
                    new_labels[lang] = label
            summary = 'copied de label to ' + ', '.join(new_labels.keys())
            page.editLabels(labels=new_labels, summary=summary)
            print(f'{qid}: ' + summary)
