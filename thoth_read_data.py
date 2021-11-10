import requests
import json
from thothlibrary import ThothClient

thoth = ThothClient()

parameters = dict(
     limit=10,
     offset=0,
     filter=''
)

response = thoth.query('works', parameters)

print(response)
