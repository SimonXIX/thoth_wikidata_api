# @name: wikidata_read_statements.py
# @version: 0.1
# @creation_date: 2021-10-21
# @license: The MIT License <https://opensource.org/licenses/MIT>
# @author: Steve Baskauf <steve.baskauf@vanderbilt.edu>
# @purpose: Retrieves all the statements for a given Wikidata entity
# @acknowledgements:
# https://github.com/HeardLibrary/digital-scholarship/blob/master/code/wikibase/api/read-statements.py

import requests
import os

#endpoint_url = os.environ.get('wikidata_url')
endpoint_url = 'https://www.wikidata.org'

entity = input("What's the Q number (including the 'Q')? ")
print('Check out ' + endpoint_url + '/wiki/' + entity + ' to see the GUI.')
resourceUrl = '/w/api.php?action=wbgetclaims&format=json&entity='+entity
uri = endpoint_url + resourceUrl
r = requests.get(uri)
data = r.json()
claims = data['claims']
print('subject: ', entity)
print()
for property, values in claims.items():
    print('property: ', property)
    for value in values:
        try:
            # print Q ID if the value is an item
            print('value: ', value['mainsnak']['datavalue']['value']['id'])
        except:
            try:
                # print the string value if the value is a literal
                print('value: ', value['mainsnak']['datavalue']['value'])
            except:
                # print the whole snak if the value is something else
                print('value: ', value['mainsnak'])
    print()
