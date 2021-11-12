import requests
import json
from thothlibrary import ThothClient

thoth = ThothClient(version="0.4.2")

response = thoth.works(limit=1)

print(json.dumps(response))
