from datetime import datetime
import requests
import json
import xmltodict
import os

url_site = "http://realtime.ridemcts.com"
url_api = "/bustime/api/v1/getpredictions"
url_request = url_site + url_api
bus_stops = '4471,4542,1417,1327'
bus_predictions = '4'

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

json_parsed = json.loads(json_response)
for bus in json_parsed['prd']:
	parsed_datetime = datetime.strptime(bus['prdtm'], '%Y%m%d %H:%M')
	formatted_datetime = datetime.strftime(parsed_datetime, '%I:%M %p')
	print bus['rt'] + "->" + bus['des'] + "\t- " + str(formatted_datetime)
