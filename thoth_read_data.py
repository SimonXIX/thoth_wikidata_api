import requests
import json
from thothlibrary import ThothClient

thoth = ThothClient(version="0.4.2")

response = thoth.works(limit=1, order='{field: PUBLICATION_DATE, direction: ASC}')

print(json.dumps(response))
