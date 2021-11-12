import requests
import json
from thothlibrary import ThothClient

thoth = ThothClient(version="0.4.2")

response = thoth.works(limit=1)

print(json.dumps(response))

# query = """query {
#     works{
#         title
#     }
# }"""
#
# url = 'https://api.thoth.pub/graphql'
# r = requests.post(url, json={'query': query})
# print(r.status_code)
# print(r.text)
