import requests
import json
import xmltodict
import os

url_site = "http://realtime.ridemcts.com"
url_api = "/bustime/api/v1/getpredictions"
url_request = url_site + url_api
bus_stop = '4471'
bus_predictions = '2'

querystring = {
	"key": os.environ['BUSTIME_API_KEY'],
	"stpid": bus_stop,
	"top": bus_predictions
}
headers = {
	'cache-control': "no-cache"
}

response = requests.request("GET", url_request, headers=headers, params=querystring)
dict_response = xmltodict.parse(response.text)

json_response = json.dumps(dict_response['bustime-response'],
							sort_keys=True,indent=4, separators=(',', ': '))
print json_response
