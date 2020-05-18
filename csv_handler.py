#!/usr/bin/env python3

import csv
import os

def create_working_dict(fileLocation):
	compiledList = csv.reader(open(fileLocation, mode='r', encoding='utf-8-sig'))

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

def create_csv(generator,filename):
	output = []
	headers = []
	user = os.getlogin()
	for i in generator:
		for a in generator[i].keys():
			if a not in headers:
				headers.append(a)

	output.append(headers)

	for x in generator:
		ind = []
		for b in generator[x].values():
			ind.append(b)
		output.append(ind)

	output_path = '/Users/' + user + '/Desktop/Output Files/' + filename + '.csv'

	with open(output_path, 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(output)
