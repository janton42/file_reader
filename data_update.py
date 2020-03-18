#!/usr/bin/python3

from csv_handler import create_working_dict, create_csv

contracts = create_working_dict('./static/contracts.csv')
costCenters = create_working_dict('./static/cost_centers.csv')
users = create_working_dict('./static/user_data.csv')

tip = {}
tipCount = 0
noEmail = {}
noEmailCount = 0
noCostCenter = {}
noCostCenterCounter = 0

for c in contracts:
	if contracts[c]['Team Name'] not in ('Ent::GTNP International Team','Ent::GTNP Leads Team','Ent::GTNP Program Manager','Ent::MS::Chrome'):
		ind = {}
		ind['cid']=contracts[c]['Contract ID']
		ind['team']=contracts[c]['Team Name']
		ind['uid']=contracts[c]['Freelancer User ID']
		ind['name']=contracts[c]['Freelancer Name']
		ind['location']=contracts[c]['Freelancer location']
		ind['start']=contracts[c]['Start Date']
		ind['end']=contracts[c]['End Date']
		ind['status']=contracts[c]['Status']
		ind['hourly_rate']=contracts[c]['Hourly Rate']
		ind['weekly_rate']=contracts[c]['Weekly Salary']
		ind['hours_limit']=contracts[c]['Weekly Limit']
		ind['manager']=contracts[c]['Contact person']
		ind['type']=contracts[c]['Contract type']
		ind['access']=contracts[c]['Systems Access']
		ind['zone']=contracts[c]['Geographic Zone']
		ind['level']=contracts[c]['Level']
		ind['category']=contracts[c]['Job Category']
		ind['cost_center']=''
		ind['email']=''
		tipCount += 1
		tip[tipCount] = ind

for u in tip:
	for cc in costCenters:
		if costCenters[cc]['Team Name'] == tip[u]['team']:
			tip[u]['cost_center'] = costCenters[cc]['Cost Center']

	for user in users:
		if users[user]['platform_id'] == tip[u]['uid'] or users[user]['full_name'] == tip[u]['name']:
			tip[u]['email'] = users[user]['upwork_email']

	if tip[u]['email'] == '':
		noEmailCount += 1
		noEmail[noEmailCount]=tip[u]
	elif tip[u]['cost_center'] == '':
		noCostCenterCounter += 1
		noCostCenter[noCostCenterCounter]=tip[u]

create_csv(tip,'tip')
create_csv(noEmail,'missing_email')
create_csv(noCostCenter,'missing_cost_center')

##user_data.csv
# AD User Name,
# full_name,
# upwork_email,
# platform_id