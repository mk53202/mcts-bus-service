import requests
import json
import xmltodict
import os
from geopy.distance import vincenty

#bus_stop_id = "4350" # Ouside 411
bus_stop_id = "4471" # Humboldt and Brady

url_stop = "http://realtime.ridemcts.com/bustime/api/v1/getstops"

querystring = {
	"key":os.environ['BUSTIME_API_KEY'],
	"format":"json",
	"stpid":bus_stop_id
}

headers = {
	'cache-control': "no-cache",
}

response = requests.request("GET", url_stop, headers=headers, params=querystring)
xml_response = xmltodict.parse(response.text)

lat = xml_response['bustime-response']['stop']['lat']
lon = xml_response['bustime-response']['stop']['lon']
bus_stop = (lat, lon)


url = "http://realtime.ridemcts.com/bustime/api/v1/getvehicles"

querystring = {
    "key":"t382wyxkgmUYuASFYtVPCRaJK",
    "format":"json",
    "rt":"14"
}

headers = {
    'cache-control': "no-cache",
    'postman-token': "7298722d-4f82-f516-243d-e7f70ccaf3fd"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print parsed_json

for vehicle in parsed_json['bustime-response']['vehicle']:
	source_bus = ( vehicle['lat'], vehicle['lon'] )
	delta_distance = int((vincenty(source_bus, bus_stop).meters))
	print vehicle['rt'] + " " + vehicle['vid'] + " " + vehicle['des'] + " " + \
		vehicle['lat'] + " " + vehicle['lon'] + " " + str(delta_distance)
