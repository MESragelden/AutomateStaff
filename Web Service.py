import json,requests

url = "https://freegeoip.app/json/"
responce = requests.request("GET",url)
print(type(responce))
json_out = json.loads(responce.text)
print(json_out.keys())
