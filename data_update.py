#!/usr/bin/python3

from csv_handler import create_working_dict, create_csv
from zone import find_zone

def tip_update():
	contracts = create_working_dict('./static/contracts.csv')
	costCenters = create_working_dict('./static/cost_centers.csv')
	users = create_working_dict('./static/user_data.csv')
	

	tip = {}
	tipCount = 0


	for c in contracts:
		loc = contracts[c]['Freelancer location'].split(',')
		if contracts[c]['Team Name'] not in (''):
			# Ent::GTNP International Team','Ent::GTNP Leads Team','Ent::GTNP Program Manager','Ent::MS::Chrome
			ind = {}
			ind['cid']=contracts[c]['Contract ID']
			ind['team']=contracts[c]['Team Name']
			ind['uid']=contracts[c]['Freelancer User ID']
			ind['name']=contracts[c]['Freelancer Name']
			ind['contract_title']=contracts[c]['Title']
			ind['full_location']=contracts[c]['Freelancer location']
			ind['country']=loc[0]
			if len(loc) == 3:
				ind['state'] = loc[1]
				ind['city'] = loc[2]
			elif len(loc) == 2:
				ind['state'] = ''
				ind['city'] = loc[1]
			else:
				ind['state'] = ''
				ind['city'] = ''
			ind['region'] = ''
			ind['start']=contracts[c]['Start Date']
			ind['end']=contracts[c]['End Date']
			ind['status']=contracts[c]['Status']
			ind['hourly_rate']=contracts[c]['Hourly Rate']
			ind['weekly_rate']=contracts[c]['Weekly Salary']
			ind['hours_limit']=contracts[c]['Weekly Limit']
			ind['manager']=contracts[c]['Contact person']
			ind['type']=contracts[c]['Contract type']
			ind['access']=contracts[c]['Systems Access']
			ind['zone_2019']=contracts[c]['Geographic Zone']
			ind['zone_2020']=''
			ind['level']=contracts[c]['Level']
			ind['category']=contracts[c]['Job Category']
			ind['cost_center']=''
			ind['email']=''
			tipCount += 1
			tip[tipCount] = ind

	for u in tip:
		tip[u]['zone_2020'] = find_zone(tip[u]['country'])

		for cc in costCenters:
			if costCenters[cc]['Team Name'] == tip[u]['team']:
				tip[u]['cost_center'] = costCenters[cc]['Cost Center']

		for user in users:
			if users[user]['platformId'] == tip[u]['uid'] or users[user]['Name'] == tip[u]['name']:
				tip[u]['email'] = users[user]['Email']

	# create_csv(tip,'tip')
		
	return tip

def missing(tip):
	noEmail = {}
	noEmailCount = 0

	noCostCenter = {}
	noCostCenterCounter = 0
	for u in tip:
		if tip[u]['email'] == '':
			noEmailCount += 1
			noEmail[noEmailCount]=tip[u]
		elif tip[u]['cost_center'] == '':
			noCostCenterCounter += 1
			noCostCenter[noCostCenterCounter]=tip[u]

	create_csv(noEmail,'missing_email')
	create_csv(noCostCenter,'missing_cost_center')

total_population = tip_update()

create_csv(total_population,'total_population')




##user_data.csv
# AD User Name,
# full_name,
# upwork_email,
# platform_id