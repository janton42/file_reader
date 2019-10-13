#!/usr/bin/env python3

import csv

from url_opener import open_url, url_builder

# class Reader(object):
# 	"""docstring for Reader"""
# 	def __init__(self, arg):
# 		super(Reader, self).__init__()
# 		self.arg = arg
		
class FileHandler(object):
	"""docstring for FileHandler"""
	
	

	def create_dict(file_location):
		compiled_list = csv.reader(open(file_location, 'r'))

		user_list = {}
		key = 0
		
		for v in compiled_list:
		   user_list[key] = v
		   key += 1

		return user_list


	def get_active_users(file_location):
	
		user_list = FileHandler.create_dict(file_location)
		complete_list = {}
		complete_list_counter = 0

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

			while i < len(headers):
				k = headers[i-1]
				if i < len(tester):
					v = tester[i-1]
				else:
					v = ''
				i += 1
				pair[k] = v
			complete_list_counter += 1
			complete_list[complete_list_counter] = pair


		return complete_list

	def get_audit_users(file_location):

		complete_list = {}
		complete_list_counter = 0

		user_list = FileHandler.create_dict(file_location)

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

	def audit(output):
	
		test_group = {}
		test_group_counter_raw = input("Enter group number to audit (1-8): ")
		test_group_counter = int(test_group_counter_raw)

		if test_group_counter > 8:
			print('Please enter a number between 1 and 8')
		else:	
			for contract in output:
				if test_group_counter == 1:
					test_group_counter += 1	
					while test_group_counter < 7:
						test_group[test_group_counter-1] = output[test_group_counter]['Contract ID']
						test_group_counter += 1
					test_group_counter += 4
				elif test_group_counter == 2:
					test_group_counter = 6
					while test_group_counter <= 10:
						test_group[test_group_counter] = output[test_group_counter+1]['Contract ID']
						test_group_counter += 1
				elif test_group_counter == 3:
					test_group_counter = 11
					while test_group_counter <= 15:
						test_group[test_group_counter] = output[test_group_counter+1]['Contract ID']
						test_group_counter += 1
				elif test_group_counter == 4:
					test_group_counter = 16
					while test_group_counter <= 20:
						test_group[test_group_counter] = output[test_group_counter+1]['Contract ID']
						test_group_counter += 1
				elif test_group_counter == 5:
					test_group_counter = 21
					while test_group_counter <= 25:
						test_group[test_group_counter] = output[test_group_counter+1]['Contract ID']
						test_group_counter += 1
				elif test_group_counter == 6:
					test_group_counter = 26
					while test_group_counter <= 30:
						test_group[test_group_counter] = output[test_group_counter+1]['Contract ID']
						test_group_counter += 1
				elif test_group_counter == 7:
					test_group_counter = 31
					while test_group_counter <= 35:
						test_group[test_group_counter] = output[test_group_counter+1]['Contract ID']
						test_group_counter += 1
				elif test_group_counter == 8:
					test_group_counter = 36
					while test_group_counter <= 40:
						test_group[test_group_counter] = output[test_group_counter+1]['Contract ID']
						test_group_counter += 1


			print(test_group)

		for contract in test_group:
			contract_id = test_group[contract]

			url = url_builder(contract_id)
			open_url(url)

	def get_active_contracts(file_location):

		complete_list = {}
		complete_list_counter = 0

		user_list = FileHandler.create_dict(file_location)

		# all_data = {}
		# user_detail_counter = 0


		# for user in user_list:

		# 	user_details = {}

		# 	ind_contract_detail = user_list.get(user)[0]
		# 	# detail_list = ind_contract_detail.split(';')

		# 	user_details['Contract Details'] = ind_contract_detail

		# 	user_detail_counter += 1

		# 	all_data[user_detail_counter] = user_details
		
		# # the length of the headers list is always 24
		headers = user_list[0]

		

		for data in user_list:
			pair = {}
			i = 1
			tester = user_list[data]

			while i < len(tester):
				k = headers[i-1]
				v = tester[i-1]
				i += 1
				pair[k] = v
			complete_list_counter += 1
			complete_list[complete_list_counter] = pair


		return complete_list


	def team_filter(complete_list):

		filtered_contracts = {}
		filter_counter = 0
		
		for c in complete_list:	
			
			parts = complete_list[c]['Team Name'].split('::')

			if len(parts) > 1:
				subteam = parts[1]
				if len(subteam) > 3:
					if subteam[0:4] != 'GTNP':
						filter_counter += 1
						filtered_contracts[filter_counter] = complete_list[c]

		return filtered_contracts

	def fte_filter(complete_list):
		filtered_users = {}
		filtered_counter = 0

		for u in complete_list:
			parts = complete_list[u]['upwork_email'].split('@')
			if len(parts) > 1:
				domain = parts[1]
				if domain != 'upwork.com':
					filtered_counter += 1
					filtered_users[filtered_counter] = complete_list[u]

		return filtered_users

	def list_compare(contract_list, user_list):
		users_without_contract = []
		
		for u in user_list:
			if u not in contract_list:
				users_without_contract.append(u)


		# for u in user_list:
		return users_without_contract


	def __init__(self, arg):
		super(FileHandler, self).__init__()
		self.arg = arg
		




