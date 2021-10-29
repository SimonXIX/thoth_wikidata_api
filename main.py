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
# How Wikidata models books: https://www.wikidata.org/wiki/Wikidata:WikiProject_Books

import requests
import thoth
import wikidata
import json
import work
import editions
import re

thoth_works = thoth.get_thoth_works()

for thoth_work in thoth_works:
    login_info = wikidata.authenticate()
    api_url = login_info[0]
    CSRF_token = login_info[1]

    # Books on Wikidata are modelled as works (the abstract written work comprising the text) and editions (a particular publication of a work)
    # First we create the work as an entity
    work_id = work.create_work(api_url, CSRF_token, thoth_work)

    # Then we write statements to that work entity to represent various metadata elements
    #response = work.write_work_statements(api_url, CSRF_token, thoth_work, work_id)
    #work.write_work_statements(api_url, CSRF_token, thoth_work, work_id)

    print('Work ID: ', work_id)

    # For however many editions there are, we create edition entities
    for publication in thoth_work['publications']:
        if publication['isbn'] is not None:
            edition_id = editions.create_edition(api_url, CSRF_token, thoth_work, work_id, publication)

            # Then we write statements to that edition entity to represent various metadata elements
            editions.write_edition_statements(api_url, CSRF_token, thoth_work, work_id, edition_id, publication)

            print('Edition ID: ', edition_id)
