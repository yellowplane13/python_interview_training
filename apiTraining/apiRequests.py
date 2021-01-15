####################
# Followed tutorial from https://www.dataquest.io/blog/python-api-tutorial/ 
###################
import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
#print(response.status_code)
jsonFile = response.json()['people']
print (jsonFile)

def jsonPrint(obj):
    op = json.dumps(obj, sort_keys=True, indent=4)
    print(op)

jsonPrint(jsonFile)