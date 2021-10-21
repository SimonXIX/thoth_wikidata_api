# @name: wikidata.py
# @version: 0.1
# @creation_date: 2021-10-21
# @license: The MIT License <https://opensource.org/licenses/MIT>
# @author: Simon Bowie <ad7588@coventry.ac.uk>
# @purpose: Performs functions against the Wikidata API
# @acknowledgements:
# Wikidata API Sandbox: https://www.wikidata.org/wiki/Special:ApiSandbox
# Wikibase authentication code: https://github.com/HeardLibrary/digital-scholarship/blob/master/code/wikibase/api/write-statements.py

import requests
import json

# Global variables
resource_url = '/w/api.php'
# Instantiate session outside of any function so that it's globally accessible.
session = requests.Session()

def get_url(path):
    with open(path, 'rt') as fileObject:
        lineList = fileObject.read().split('\n')
    endpoint_url = lineList[0].split('=')[1]
    api_url = endpoint_url + resource_url
    return api_url

def authenticate(path):
    with open(path, 'rt') as fileObject:
        lineList = fileObject.read().split('\n')
    endpoint_url = lineList[0].split('=')[1]
    username = lineList[1].split('=')[1]
    password = lineList[2].split('=')[1]
    api_url = endpoint_url + resource_url

    # Request for token for data-modifying actions
    # https://www.wikidata.org/w/api.php?action=help&modules=query%2Btokens
    parameters = dict(
        format='json',
        action='query',
        meta='tokens',
        type='login'
    )
    r = session.get(url=api_url, params=parameters)
    json = r.json()
    login_token = json['query']['tokens']['logintoken']

    # The result of this part is a successful session login.
    # See example at https://www.mediawiki.org/wiki/API:Login
    parameters = dict(
        format='json',
        action='login',
        lgname=username,
        lgpassword=password,
        lgtoken=login_token
    )
    r = session.post(api_url, data=parameters)

    # The CSRF (edit) token is an edit token that is actually used to authorize particular write actions
    # It is used to prevent cross-site request forgery (csrf) attacks. I think it's primarily relevant when web forms are used
    # Here's the page that shows how to get an edit token
    # https://www.mediawiki.org/wiki/API:Edit
    parameters = dict(
        action='query',
        meta='tokens',
        format='json'
    )
    r = session.get(url=api_url, params=parameters)
    data = r.json()
    # The response looks like this:
    # {'batchcomplete': '', 'query': {'tokens': {'csrftoken': '6bc490bb0d2e78cb3f8a2b94e8159da85cdc2484+\\'}}}
    CSRF_token = data['query']['tokens']['csrftoken']
    return [CSRF_token, api_url]

def create_entity(edit_token, api_url, data_string):

    parameters = {
        'action': 'wbeditentity',
        'format': 'json',
        'new': 'item',
        'token': edit_token,
        # note: the data value is a string. I think it will get URL encoded by requests before posting
        'data': data_string
    }
    r = session.post(api_url, data=parameters)
    response = r.text
    if response[2:7] == 'error':
        print(response)
        return "error"
    else:
        data = r.json()
        return data["entity"]["id"]

# pass in the local names including the initial letter as strings, e.g. ('Q3345', 'P6', 'Q1917')
def write_statement(edit_token, api_url, subjectQNumber, propertyPNumber, objectQNumber):
    strippedQNumber = objectQNumber[1:len(objectQNumber)] # remove initial "Q" from object string
    parameters = {
        'action':'wbcreateclaim',
        'format':'json',
        'entity':subjectQNumber,
        'snaktype':'value',
        'bot':'1',  # not sure that this actually does anything
        'token': edit_token,
        'property': propertyPNumber,
        # note: the value is a string, not an actual data structure.  I think it will get URL encoded by requests before posting
        'value':'{"entity-type":"item","numeric-id":' + strippedQNumber+ '}'
    }
    r = session.post(api_url, data=parameters)
    data = r.json()
    return data
