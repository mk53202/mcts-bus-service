import requests
import json
import xmltodict
import os

url_site = "http://realtime.ridemcts.com"
url_api = "/bustime/api/v1/getdirections"
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

json_response = json.dumps(dict_response['bustime-response'],
							sort_keys=True,indent=4, separators=(',', ': '))
print json_response
