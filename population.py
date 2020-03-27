#!/usr/bin/python3

from data_update import tip_update, missing
from csv_handler import create_csv

updated_tip = tip_update()

def country_count():
	countries = []
	countries_count = {}
	counter = 0

	for i in updated_tip:
		country = updated_tip[i]['country']
		if country not in countries:
			countries.append(country)

	for x in countries:
		ind = {}
		count = 0
		for a in updated_tip:
			country = updated_tip[a]['country']
			if country == x:
				count += 1
		ind['country'] = x
		ind['count'] = count
		counter += 1
		countries_count[counter] = ind

	return countries_count

create_csv(country_count(), 'country_count')

def state_count():
	states = []
	states_count = {}
	counter = 0

	for i in updated_tip:
		state = updated_tip[i]['state']
		if state not in states:
			states.append(state)

	for x in states:
		ind = {}
		count = 0
		if x != '':
			for a in updated_tip:
				country = updated_tip[a]['country']
				state = updated_tip[a]['state']	
				if state == x:
					count += 1
			ind['state'] = x
			ind['count'] = count
			counter += 1
			states_count[counter] = ind

	return states_count

create_csv(state_count(),'state_count')