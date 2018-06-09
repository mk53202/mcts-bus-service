import requests
import json
import xmltodict
import os

url_site = "http://realtime.ridemcts.com"
url_api = "/bustime/api/v1/getstops"
url_request = url_site + url_api
bus_routes = 'GRE'
bus_direction = 'NORTH'
querystring = {
	"key": os.environ['BUSTIME_API_KEY'],
	"rt": bus_routes,
	"dir": bus_direction
}
headers = {
	'cache-control': "no-cache"
}

response = requests.request("GET", url_request, headers=headers, params=querystring)
dict_response = xmltodict.parse(response.text)

json_response = json.dumps(dict_response['bustime-response'],
							sort_keys=True,indent=4, separators=(',', ': '))
print json_response
