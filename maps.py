#!/usr/bin/env python3

import requests
import datetime

now = datetime.datetime.now()

date = now.strftime('%Y-%m-%d')

mapUrl = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

loc = input('\nPlease enter a location:\n')

querystring = {"language":"en","address":loc}

headers = {
    'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
    'x-rapidapi-key': "3e250ebe58msh61574e3e1eacef3p1c9de8jsn44dc33d0649b"
    }

mapResponse = requests.request("GET", mapUrl, headers=headers, params=querystring).json()

for i in mapResponse['results']:
	lat = str(i['geometry']['location']['lat'])
	lng = str(i['geometry']['location']['lng'])

latlng = lat + ',' + lng

print('Google querystring: ', querystring)
print('Coordinates: ', latlng)
response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={"Authorization": "Bearer Y3uOU65X4pJYa-CpHLI5z6nkx1APoaLEM_01lQo9"},
    params={"relevance": "location_around, start_around",
            "location_around.origin": latlng,
            "location_around.offset": "1km",
            "start_around.origin": date,
            "category": "terror, disasters",
            "active.gte": date
            }
)
relEvents = []

# print(response.json())

for i in response.json()['results']:
    if i['relevance'] != 0:
        relevance = i['relevance']
        labels = i['labels']
        rank = i['rank']
        start = i['start']
        location = i['location']
        country = i['country']
        relEvent = {}
        relEvent['relevance'] = relevance
        relEvent['labels'] = labels
        relEvent['rank'] = rank
        relEvent['start'] = start
        relEvent['location'] = location
        relEvent['country'] = country
        relEvents.append(relEvent)
        # print('id: ',i['id'])
        # print('title: ',i['title'])
        # print('description: ',i['description'])
        # print('category: ',i['category'])
        # print('local_rank: ',i['local_rank'])
        # print('entities: ',i['entities'])
        # print('duration: ',i['duration'])
        # print('end: ',i['end'])
        # print('updated: ',i['updated'])
        # print('first_seen: ',i['first_seen'])
        # print('timezone: ',i['timezone'])
        # print('scope: ',i['scope'])
        # print('place_hierarchies: ',i['place_hierarchies'])
        # print('state: ',i['state'])

if len(relEvents) > 0:
    print(len(relEvents))
    for i in relEvents:
        print(i)
else:
    print('No Relevant Events Found')


