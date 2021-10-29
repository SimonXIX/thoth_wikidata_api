import requests
import json
from thothlibrary import ThothClient

thoth = ThothClient()

parameters = dict(
    limit=1,
    offset=0,
    filter=''
)

response = thoth.query('works', parameters)

print(response)
