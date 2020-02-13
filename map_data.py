#!/usr/bin/env python3

import requests

eventResponse = requests.get(
	url = 'https://api.predicthq.com/v1/events/',
	headers = {'Authorization': 'Bearer Y3uOU65X4pJYa-CpHLI5z6nkx1APoaLEM_01lQo9'},
	params = {'q': 'jazz', 'country':'US', 'active.gte': '2020-02-12', 'active.lte': '2020-02-24', 'active.tz': 'America/Los_Angeles'
	}
	)

formatted = []

for a in eventResponse.json()['results']:
	lat = str(a['location'][1])
	lng = str(a['location'][0])
	latlng = lat + ',' + lng
	formatted.append(latlng)

mapUrl = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

for b in formatted:
	querystring = {"language":"en","latlng": b}

	headers = {
	    'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
	    'x-rapidapi-key': "3e250ebe58msh61574e3e1eacef3p1c9de8jsn44dc33d0649b"
	    }

	mapResponse = requests.get(mapUrl, headers=headers, params=querystring).json()['results'][0]['address_components']


	for i in mapResponse:
		if 'locality' in i['types'] and 'political' in i['types']:
			print(i['long_name'])



