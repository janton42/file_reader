#!/usr/bin/env python3

import requests

response = requests.get(
	url = 'https://api.predicthq.com/v1/events/',
	headers = {'Authorization': 'Bearer Y3uOU65X4pJYa-CpHLI5z6nkx1APoaLEM_01lQo9'},
	params = {'q': 'jazz', 'country':'US', 'active.gte': '2020-02-12', 'active.lte': '2020-02-24', 'active.tz': 'America/Los_Angeles'
	}
	)

for i in response.json()['results']:
	print('Title: ' + i['title'])


