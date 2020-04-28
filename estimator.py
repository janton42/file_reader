#!/usr/bin/python3

from csv_handler import create_working_dict, create_csv
from zone import find_zone

regions = create_working_dict('./static/regions.csv')
rates = create_working_dict('./static/rates.csv')


def estimate(rate_card,region_card):
	output = {}
	out_counter = 0

	for c in region_card:
		ind = {}
		country = region_card[c]['Country']
		ind['country'] = country
		ind['region'] = region_card[c]['Region']
		ind['zone'] = find_zone(country)
		out_counter += 1
		output[out_counter] = ind



	return output




create_csv(estimate(rates,regions),'estimate')

# 	return output