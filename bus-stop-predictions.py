import requests
import json
import xmltodict
import os

url_site = "http://realtime.ridemcts.com"
url_api = "/bustime/api/v1/getpredictions"
url_request = url_site + url_api
bus_stops = '4471,4542,1417,1327'
bus_predictions = '4'
# bus_predictions = ''

querystring = {
	"key": os.environ['BUSTIME_API_KEY'],
	"stpid": bus_stops,
	"top": bus_predictions
}
headers = {
	'cache-control': "no-cache"
}

response = requests.request("GET", url_request, headers=headers, params=querystring)
dict_response = xmltodict.parse(response.text)

json_response = json.dumps(dict_response['bustime-response'],
							sort_keys=True,indent=4, separators=(',', ': '))

# print "JSON:\n" + json_response

# print "JSON_PARSED:\n"
json_parsed = json.loads(json_response)
for line in json_parsed['prd']:
	print line['rt'] + " -> " + line['des'] + " - " + line['prdtm']

# ['des']
# for destination in json_response:
# 	print destination.['des']
