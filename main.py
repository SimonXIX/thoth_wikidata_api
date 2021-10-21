import requests
import thoth
import wikidata

# Global variables
config_file_path = 'config.env'

thoth_works = thoth.get_thoth_works()

for thoth_work in thoth_works:
    parsed_work = thoth.parse_thoth_work(thoth_work)
    login_info = wikidata.authenticate(config_file_path)
    CSRF_token = login_info[0]
    api_url = login_info[1]

    #entity_id = wikidata.create_entity(CSRF_token, api_url, parsed_work)

    #sub = entity_id # subject entity
    sub = 'Q222821' # subject entity
    prop = 'P82' # property
    obj = 'Q131598' # object entity

    response = wikidata.write_statement(CSRF_token, api_url, sub, prop, obj)

    print(response)
