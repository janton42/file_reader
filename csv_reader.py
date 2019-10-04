#!/usr/bin/env python3

import csv

# class Reader(object):
# 	"""docstring for Reader"""
# 	def __init__(self, arg):
# 		super(Reader, self).__init__()
# 		self.arg = arg
		

def get_active_users(file_location):

	
	compiled_list = csv.reader(open(file_location, 'r'))
	
	complete_list = {}
	complete_list_counter = 0

	user_list = {}
	key = 0
	
	for v in compiled_list:
	   user_list[key] = v
	   key += 1

	all_data = {}
	user_detail_counter = 0


	for user in user_list:

		user_details = {}

		ind_user_detail = user_list.get(user)[0]
		detail_list = ind_user_detail.split(';')

		user_details['User Details'] = detail_list

		user_detail_counter += 1

		all_data[user_detail_counter] = user_details
	
	# the length of the headers list is always 24
	headers = all_data[1]['User Details']

	

	for data in all_data:
		pair = {}
		i = 1
		tester = all_data[data]['User Details']

		while i < len(tester):
			k = headers[i]
			v = tester[i]
			i += 1
			pair[k] = v
		complete_list_counter += 1
		complete_list[complete_list_counter] = pair


	return complete_list


def get_audit_users(file_location):

	compiled_list = csv.reader(open(file_location, 'r'))
	complete_list = {}
	complete_list_counter = 0

	user_list = {}
	key = 0
	
	for v in compiled_list:
	   user_list[key] = v
	   key += 1

	all_data = {}
	user_detail_counter = 0


	for user in user_list:

		user_details = {}

		ind_user_detail = user_list.get(user)
		ind_user_detail.append(False)

		user_details['User Details'] = ind_user_detail

		user_detail_counter += 1

		all_data[user_detail_counter] = user_details
	
	
	headers = all_data[1]['User Details']
	del headers[-1]
	headers.append('Audited')

	

	for data in all_data:
		pair = {}
		i = 0
		tester = all_data[data]['User Details']

		while i < len(tester):
			k = headers[i]
			v = tester[i]
			i += 1
			pair[k] = v
		complete_list_counter += 1
		complete_list[complete_list_counter] = pair


	return complete_list

def audit_status_changer(contract):
	if contract['Audited'] == False:
		contract['Audited'] = True

	elif contract['Audited'] == True:
		contract['Audited'] = False



