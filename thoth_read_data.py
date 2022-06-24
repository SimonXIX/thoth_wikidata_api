import requests
import json
from thothlibrary import ThothClient

thoth = ThothClient()

response = thoth.works(limit=1, order='{field: PUBLICATION_DATE, direction: ASC}')
#response = thoth.works()

print(json.dumps(response))
