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

# Global variables
config_file_path = 'config.env'

thoth_works = thoth.get_thoth_works()

for thoth_work in thoth_works:
    parsed_work = thoth.parse_thoth_work(thoth_work)
    login_info = wikidata.authenticate(config_file_path)
    api_url = login_info[0]
    CSRF_token = login_info[1]

    #entity_id = wikidata.create_entity(api_url, CSRF_token, parsed_work)

    #sub = entity_id # subject entity
    sub = 'Q222821' # subject entity
    prop = 'P82' # property
    obj = 'Q131598' # object entity

    #response = wikidata.write_statement(api_url, CSRF_token, sub, prop, obj)

    #response = wikidata.delete_entity(api_url, CSRF_token, 'Q222821')

    print(response)
