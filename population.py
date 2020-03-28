#!/usr/bin/python3

from data_update import tip_update, missing
from csv_handler import create_csv


class PopulationTabulator(object):
	"""docstring for PopulationTabulator"""
	updated_tip = tip_update()

	def country_count():
		countries = []
		countries_count = {}
		counter = 0

		for i in PopulationTabulator.updated_tip:
			country = PopulationTabulator.updated_tip[i]['country'].strip()
			if country not in countries:
				countries.append(country)

		for x in countries:
			ind = {}
			count = 0
			for a in PopulationTabulator.updated_tip:
				country = PopulationTabulator.updated_tip[a]['country'].strip()
				if country == x:
					count += 1
			ind['country'] = x
			ind['count'] = count
			counter += 1
			countries_count[counter] = ind

		

		return countries_count

	

	def state_list():
		states = []

		for i in PopulationTabulator.updated_tip:
			country = PopulationTabulator.updated_tip[i]['country']
			state = PopulationTabulator.updated_tip[i]['state'].strip()
			if state not in states and state != '' and country == 'United States':
				states.append(state)

		return sorted(states)

	def state_count(states):
		states_count = {}
		counter = 0
		all_states = []

		for i in PopulationTabulator.updated_tip:
			if PopulationTabulator.updated_tip[i]['country'] == 'United States' and PopulationTabulator.updated_tip[i]['state'] != '':
				state = PopulationTabulator.updated_tip[i]['state'].strip()
				all_states.append(state)

		for x in states:
			ind = {}
			count = all_states.count(x)
			ind['state'] = x
			ind['count'] = count
			counter += 1
			states_count[counter] = ind

		return states_count

	

	def detail_states(states):
		states_details = {}
		counter = 0
		for x in PopulationTabulator.updated_tip:
			ind = {}
			if PopulationTabulator.updated_tip[x]['state'].strip() in states:
				counter +=1
				states_details[counter] = PopulationTabulator.updated_tip[x]
		

		return states_details

	
	# usStatesDetail = create_csv(PopulationTabulator.detail_states(PopulationTabulator.state_list()),'us_state_details_all')
	# usStatesCount=create_csv(PopulationTabulator.state_count(PopulationTabulator.state_list()),'us_states_count')
	# countryCount=create_csv(PopulationTabulator.country_count(),'country_count')

	def __init__(self, arg):
		super(PopulationTabulator, self).__init__()
		self.arg = arg
		

