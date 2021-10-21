# @name: main.py
# @version: 0.1
# @creation_date: 2021-10-21
# @license: The MIT License <https://opensource.org/licenses/MIT>
# @author: Simon Bowie <ad7588@coventry.ac.uk>
# @purpose: Retrieves a Thoth work and creates a Wikidata entry from that metadata
# @acknowledgements:
# Wikidata API Sandbox: https://www.wikidata.org/wiki/Special:ApiSandbox
# Wikibase authentication code: https://github.com/HeardLibrary/digital-scholarship/blob/master/code/wikibase/api/write-statements.py
# Thoth API client: https://github.com/thoth-pub/thoth-client

import requests
import thoth
import wikidata
import os

thoth_works = thoth.get_thoth_works()

for thoth_work in thoth_works:
    parsed_work = thoth.parse_thoth_work(thoth_work)
    login_info = wikidata.authenticate()
    api_url = login_info[0]
    CSRF_token = login_info[1]

    # create entity for the work
    #entity_id = wikidata.create_entity(api_url, CSRF_token, parsed_work)

    # insert statements for the work's various properties
    # first, get the Wikidata property values: these differ between test.wikidata.org and wikidata.org so are set in the config file passed through Docker Compose
    property_values = wikidata.get_property_values()

    # insert statement for 'instance of book'
    #sub = entity_id # subject entity
    sub = 'Q222821' # subject entity
    prop = property_values['instance_of'] # property
    obj = 'Q131598' # object entity
    #response = wikidata.write_statement(api_url, CSRF_token, sub, prop, obj)

    # insert statement for 'title'
    #sub = entity_id # subject entity
    sub = 'Q222821' # subject entity
    prop = property_values['title'] # property
    obj = thoth_work['fullTitle'] # object entity
    #response = wikidata.write_statement(api_url, CSRF_token, sub, prop, obj)

    # insert statement for 'publication date'
    #sub = entity_id # subject entity
    sub = 'Q222821' # subject entity
    prop = property_values['publication_date'] # property
    obj = thoth_work['publicationDate'] # object entity
    #response = wikidata.write_statement(api_url, CSRF_token, sub, prop, obj)

    #response = wikidata.delete_entity(api_url, CSRF_token, 'Q222821')

    print(response)
