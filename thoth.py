# @name: thoth.py
# @version: 0.1
# @creation_date: 2021-10-21
# @license: The MIT License <https://opensource.org/licenses/MIT>
# @author: Simon Bowie <ad7588@coventry.ac.uk>
# @purpose: Performs functions against the Thoth API
# @acknowledgements:
# Thoth API client: https://github.com/thoth-pub/thoth-client

import requests
import json
from thothlibrary import ThothClient

def get_thoth_works():
    thoth = ThothClient()

    parameters = dict(
        limit=1,
        offset=0,
        filter=''
    )

    response = thoth.query('works', parameters)
    #for work in response:
    #     work_data = dict(
    #         title=work['fullTitle'],
    #         publication_date=work['publicationDate'],
    #         license=work['license'],
    #         copyright_holder=work['copyrightHolder'],
    #         doi=work['doi']
    #     )
    #     for contributions in work['contributions']:
    #         contributor_type = contributions['contributionType']
    #         work_data[contributor_type]=contributions['fullName']
    #     for publications in work['publications']:
    #         isbn_type = publications['publicationType']
    #         work_data['isbn_' + isbn_type]=publications['isbn']
    # print(work_data)
    return response

# turn a work from Thoth into a JSON string suitable for submitting to the Wikidata API
def parse_thoth_work(work):
    label_list = [
        {'language': 'en', 'string': work['fullTitle']},
        {'language': 'en-gb', 'string': work['fullTitle']}
    ]
    # note that descriptions on Wikidata must be no more than 250 characters long
    description_list = [
        {'language': 'en', 'string': 'Punctum Books work'}
    ]

    # the data passed to the Wikidata API must be JSON in string form.  Because of Python's use of curly braces in format strings, it's
    # best to create the data to be passed as a dictionary, then use json.dumps to convert it into string form.
    # Here's what we are building:
    '''
    dataDict = {
        "labels":{
            "en":{"language":"en","value":"Simon Worthington"},
            "fr":{"language":"fr","value":"Simon Worthington"},
            "de":{"language":"de","value":"Simon Worthington"}
            },
        "descriptions":{
            "en":{"language":"en","value":"Publishing technology researcher"}
            "fr":{"language":"fr","value":"Chercheur en technologie de l'édition"},
            "de":{"language":"de","value":"Verlagstechnologie-Forscher"}
            }
        }
    '''
    dataDict = {}

    innerDict = {}
    for label in label_list:
        innerDict[label['language']] = {"language": label['language'], "value": label['string']}
    dataDict['labels'] =  innerDict

    innerDict = {}
    for description in description_list:
        innerDict[description['language']] = {"language": description['language'], "value": description['string']}
    dataDict['descriptions'] =  innerDict

    dataString = json.dumps(dataDict)

    return dataString
