#!/usr/bin/env python3

import requests

mapUrl = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

querystring = {"language":"en","address":"New York"}

headers = {
    'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
    'x-rapidapi-key': "3e250ebe58msh61574e3e1eacef3p1c9de8jsn44dc33d0649b"
    }

mapResponse = requests.request("GET", mapUrl, headers=headers, params=querystring).json()

for i in mapResponse['results']:
	lat = str(i['geometry']['location']['lat'])
	lng = str(i['geometry']['location']['lng'])

latlng = lat + ',' + lng

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={"Authorization": "Bearer Y3uOU65X4pJYa-CpHLI5z6nkx1APoaLEM_01lQo9"},
    params={"relevance": "rank,q,start_around,location_around",
            "location_around.origin": latlng,
            "location_around.offset": "1km",
            "start_around.origin": "2020-02-12",
            "q": "jazz",
            "category": "concerts",
            "active.gte": "2020-02-12"}
)

print(response.json())
