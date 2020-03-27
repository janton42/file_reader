#!/usr/bin/python3

from data_update import tip_update, missing
from csv_handler import create_csv

updated_tip = tip_update()

def country_count():
	countries = []
	countries_count = {}
	counter = 0

	for i in updated_tip:
		country = updated_tip[i]['country'].strip()
		if country not in countries:
			countries.append(country)

	for x in countries:
		ind = {}
		count = 0
		for a in updated_tip:
			country = updated_tip[a]['country'].strip()
			if country == x:
				count += 1
		ind['country'] = x
		ind['count'] = count
		counter += 1
		countries_count[counter] = ind

	return countries_count

# create_csv(country_count(), 'country_count')

def state_list():
	states = []

	for i in updated_tip:
		country = updated_tip[i]['country']
		state = updated_tip[i]['state'].strip()
		if state not in states and state != '' and country == 'United States':
			states.append(state)

	return sorted(states)

def state_count(states):
	states_count = {}
	counter = 0
	all_states = []

	for i in updated_tip:
		if updated_tip[i]['country'] == 'United States' and updated_tip[i]['state'] != '':
			state = updated_tip[i]['state'].strip()
			all_states.append(state)

	for x in states:
		ind = {}
		count = all_states.count(x)
		ind['state'] = x
		ind['count'] = count
		counter += 1
		states_count[counter] = ind

	return states_count

create_csv(state_count(state_list()),'us_states_count')

# create_csv(state_count(state_list()),'state_count')