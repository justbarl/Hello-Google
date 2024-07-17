import requests

Response = requests.get('https://google.com')
print(Response.text)
