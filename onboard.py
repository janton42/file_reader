#!/usr/bin/env python3

from csv_reader import *

def createWorkingDict(fileLocation):
	compiledList = csv.reader(open(fileLocation, 'r'))

	dictList = {}
	key = 0
	
	for v in compiledList:
	   dictList[key] = v
	   key += 1

	headers = dictList[0]

	del dictList[0]

	labeled = {}
	labeledCounter = 1

	for i in dictList:
		pair = {}
		x = 0
		while x < len(headers):
			k = headers[x]
			v = dictList[i][x]
			pair[k] = v
			x += 1
		labeled[labeledCounter] = pair
		labeledCounter += 1


	return labeled


def createCsv(generator):
	output = []

	for i in generator:
		output.append(i)

	output_path = '/Users/jeffstock/Desktop/Output Files/rates.csv'

	with open(output_path, 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(output)

hiverData = createWorkingDict('./static/hiver_analytics.csv')
contractData = createWorkingDict('./static/contracts.csv')
valChart = createWorkingDict('./static/date_values_chart.csv')

uniqueOffers = []

offers = {}
offerCounter = 0

for a in hiverData:
	hiverName = hiverData[a]['SUBJECT'].split(' ')
	received = hiverData[a]['CREATED_AT_TIMESTAMP'].split(' ')[0]
	if len(hiverName) > 3 and hiverName[2] == 'Evaluation':
		ind = {}
		firstName = hiverName[4]
		lastInit = hiverName[5][0]
		name = firstName,lastInit
		for v in valChart:
			if received == valChart[v]['Date']:
				ind['name'] = name
				ind['received'] = received
				ind['value'] = valChart[v]['Value']
		offers[offerCounter] = ind
		offerCounter += 1

for i in offers:
	comp = offers[i]['name'][0] + ' ' + offers[i]['name'][1] + ' ' + offers[i]['value']
	if comp not in uniqueOffers:
		uniqueOffers.append(comp)

uOffers = {}
uOffersCounter = 0

for a in uniqueOffers:
	offer = {}
	offer['name'] = a.split(' ')[0] + ' ' + a.split(' ')[1]
	offer['value'] = a.split(' ')[2]
	uOffers[uOffersCounter] = offer
	uOffersCounter += 1

for u in uOffers:
	print(uOffers[u])

starts = {}
startsCounter = 0

for i in contractData:
	name = contractData[i]['Freelancer Name'].split(' ')[0] + ' ' + contractData[i]['Freelancer Name'].split(' ')[1][0]

	start = contractData[i]['Start Date'].split('T')[0]

	if start >= '2020-01-01':
		for v in valChart:
			if start == valChart[v]['Date']:
				ind = {}
				ind['name'] = name
				ind['value'] = valChart[v]['Value']
				ind['cid'] = contractData[i]['Contract ID']
				ind['start'] = contractData[i]['Start Date']
		starts[startsCounter] = ind
		startsCounter += 1

uniqueStarts = []

totalStarts = 0
totalTime = 0

for x in starts:
	for y in uOffers:
		if starts[x]['name'] == uOffers[y]['name']:
			difference = int(starts[x]['value']) - int(uOffers[y]['value'])
			totalStarts += 1
			totalTime += difference
			print('Start Date',starts[x]['start'].split('T')[0],'CID: ', starts[x]['cid'] ,'Name: ',starts[x]['name'], 'Offer Value: ', uOffers[y]['value'], 'Start Value: ', starts[x]['value'], 'Difference: ', difference)

average = totalTime/totalStarts
days = round(average,0)
hours = round((average - days)*24,0) + (days * 24)

print('Total Starts: ', totalStarts, '\nTotal Days: ',totalTime, '\nTotal Average: ', average, '\nAverage Days: ', days, '\nAverage Hours: ', hours)


