import requests
import json
import xmltodict
import os

url_site = "http://realtime.ridemcts.com"
url_api = "/bustime/api/v1/gettime"
url_request = url_site + url_api
querystring = {
	"key":os.environ['BUSTIME_API_KEY']
}
headers = {
	'cache-control': "no-cache"
}

response = requests.request("GET", url_request, headers=headers, params=querystring)
my_dict = xmltodict.parse(response.text)

print my_dict['bustime-response']['tm']

# JSON export
my_json = json.dumps(my_dict['bustime-response']['tm'],
							sort_keys=True,indent=4, separators=(',', ': '))
print my_json
