import requests
import json
import xmltodict
import os

url_site = "http://realtime.ridemcts.com"
url_api = "/bustime/api/v1/getvehicles"
url_request = url_site + url_api
bus_routes = '14'
querystring = {
	"key": os.environ['BUSTIME_API_KEY'],
	"rt": bus_routes
}
headers = {
	'cache-control': "no-cache"
}

response = requests.request("GET", url_request, headers=headers, params=querystring)
dict_response = xmltodict.parse(response.text)

parsed_buses = []

for item in dict_response['bustime-response']['vehicle']:
	# parsed_buses.append(item['vid'], item['lat'], item['lon'])
	parsed_buses = item['vid'] + item['lat'] + item['lon']
	# print item

print parsed_buses

# json_response = json.dumps(dict_response['bustime-response']['vehicle'],
# 							sort_keys=True,indent=4, separators=(',', ': '))
# print json_response
