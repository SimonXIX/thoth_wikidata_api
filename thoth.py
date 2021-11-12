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
    thoth = ThothClient(version="0.4.2")

    response = thoth.works(limit=1, order='{field: PUBLICATION_DATE, direction: ASC}')

    return response

# turn a work from Thoth into a JSON string suitable for submitting to the Wikidata API
def parse_thoth_work(work):
    label_list = [
        {'language': 'en', 'string': work['fullTitle']},
        {'language': 'en-gb', 'string': work['fullTitle']}
    ]
    # note that descriptions on Wikidata must be no more than 250 characters long
    description_list = [
        {'language': 'en', 'string': 'Work from Thoth'},
        {'language': 'en-gb', 'string': 'Work from Thoth'}
    ]

    # the data passed to the Wikidata API must be JSON in string form.  Because of Python's use of curly braces in format strings, it's
    # best to create the data to be passed as a dictionary, then use json.dumps to convert it into string form.
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

# turn an edition from Thoth into a JSON string suitable for submitting to the Wikidata API
def parse_thoth_edition(work, publication):
    label_list = [
        {'language': 'en', 'string': work['fullTitle'] + ' (' + publication['publicationType'].lower() + ' edition)'},
        {'language': 'en-gb', 'string': work['fullTitle'] + ' (' + publication['publicationType'].lower() + ' edition)'}
    ]
    # note that descriptions on Wikidata must be no more than 250 characters long
    description_list = [
        {'language': 'en', 'string': publication['publicationType'].capitalize() + ' edition of work from Thoth'},
        {'language': 'en-gb', 'string': publication['publicationType'].capitalize() + ' edition of work from Thoth'}
    ]

    # the data passed to the Wikidata API must be JSON in string form.  Because of Python's use of curly braces in format strings, it's
    # best to create the data to be passed as a dictionary, then use json.dumps to convert it into string form.
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

# turn a person from a Thoth work into a JSON string suitable for submitting to the Wikidata API
def parse_person(contributor):
    label_list = [
        {'language': 'en', 'string': contributor['fullName']},
        {'language': 'en-gb', 'string': contributor['fullName']}
    ]
    # note that descriptions on Wikidata must be no more than 250 characters long
    description_list = [
        {'language': 'en', 'string': contributor['contributionType'].capitalize()},
        {'language': 'en-gb', 'string': contributor['contributionType'].capitalize()}
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
