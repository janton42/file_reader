#!/usr/bin/env python3

import csv
from url_opener import open_url, url_builder
import datetime

# class Reader(object):
# 	"""docstring for Reader"""
# 	def __init__(self, arg):
# 		super(Reader, self).__init__()
# 		self.arg = arg
		
class FileHandler(object):
	now = datetime.datetime.now()
	"""docstring for FileHandler"""
	complete_list = {}
	complete_list_counter = 0	
	

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

		a = FileHandler.complete_list
		b = FileHandler.complete_list_counter

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
			b += 1
			a[b] = pair


		return a

	def get_audit_users(file_location):

		a = FileHandler.complete_list
		b = FileHandler.complete_list_counter

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
		
		# headers.append('Audited')

		

		for data in all_data:
			pair = {}
			i = 0
			tester = all_data[data]['User Details']

			while i < len(tester):
				k = headers[i]
				v = tester[i]
				i += 1
				pair[k] = v
			b += 1
			a[b] = pair


		return a

	def get_active_contracts(file_location):

		# complete_list = {}
		# complete_list_counter = 0

		user_list = FileHandler.create_dict(file_location)

		headers = user_list[0]

		a = FileHandler.complete_list
		b = FileHandler.complete_list_counter
		

		for data in user_list:
			pair = {}
			i = 1
			tester = user_list[data]

			while i < len(tester):
				k = headers[i-1]
				v = tester[i-1]
				i += 1
				pair[k] = v
			b += 1
			a[b] = pair


		return a

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

	def find_users_without_contracts(active_contracts, auwa):

		uids_contracts = []
		uids_users = []

		names_contracts = []
		names_users = []

		for c in active_contracts:
			uids_contracts.append(active_contracts[c]['Freelancer User ID'])
			names_contracts.append(active_contracts[c]['Freelancer Name'])

		for u in auwa:
			uids_users.append(auwa[u]['worker_user_id'])
			names_users.append(auwa[u]['full_name'])

		filtered_by_uid = FileHandler.find_missing_from_list(uids_contracts,uids_users)
		filtered_by_name = FileHandler.find_missing_from_list(names_contracts,names_users)

		details = {}
		details_counter = 0

		for u in filtered_by_uid:
			for au in auwa:
				uid = auwa[au]['worker_user_id']
				if u == uid:
					details_counter += 1
					details[details_counter] = auwa[au]
		
		filtered_by_name_and_cid = {}
		filtered_by_name_and_cid_counter = 0

		for u in filtered_by_name:
			for au in details:
				u_name = details[au]['full_name']
				if u == u_name:
					filtered_by_name_and_cid_counter += 1
					filtered_by_name_and_cid[filtered_by_name_and_cid_counter] = details[au]

		output = [['worker_user_id','full_name','upwork_email']]

		for i in filtered_by_name_and_cid:
			action_item = []
			action_item.append(filtered_by_name_and_cid[i]['worker_user_id'])
			action_item.append(filtered_by_name_and_cid[i]['full_name'])
			action_item.append(filtered_by_name_and_cid[i]['upwork_email'])
			output.append(action_item)

		return output

	def find_end_dates(active_contracts):
		action_items = {}
		action_items_counter = 0
		now = datetime.datetime.now()

		date = now.strftime('%Y/%m/%d')

		for c in active_contracts:
			expired = {}
			expires_today = {}
			next_14 = {}

			if active_contracts[c]['End Date'] == 'End Date' or active_contracts[c]['End Date'] == '':
				end_year = 0
			else:
				end_year_raw = active_contracts[c]['End Date'][0:4]
				end_year = int(end_year_raw)
				end_month_raw = active_contracts[c]['End Date'][5:7]
				end_month = int(end_month_raw)
				end_day_raw = active_contracts[c]['End Date'][8:10]
				end_day = int(end_day_raw)


			# Expired contracts

			if end_year == now.year -1 or end_year == now.year -2 or end_year == now.year and end_month == now.month and end_day < now.day:
				action_items_counter += 1
				expired['Contract ID'] = active_contracts[c]['Contract ID']
				expired['Freelancer Name'] = active_contracts[c]['Freelancer Name']
				expired['End Date'] = active_contracts[c]['End Date'][0:10]
				expired['Contract Status'] = active_contracts[c]['Status']
				expired['Expired'] = 'Yes'
				expired['Expires Today'] = 'No'

			
				action_items[c] = expired


			# Contracts ending today

			elif end_year == now.year and end_month == now.month and end_day == now.day:
				action_items_counter += 1
				expires_today['Contract ID'] = active_contracts[c]['Contract ID']
				expires_today['Freelancer Name'] = active_contracts[c]['Freelancer Name']
				expires_today['End Date'] = active_contracts[c]['End Date'][0:10]
				expires_today['Contract Status'] = active_contracts[c]['Status']
				expires_today['Expired'] = 'No'
				expires_today['Expires Today'] = 'Yes'

				action_items[c] = expires_today

			# Contracts ending this month in the next 14 days (starting tomorrow)

			elif end_year == now.year and end_month == now.month and end_day > now.day and end_day < (now.day + 14):
				action_items_counter += 1
				next_14['Contract ID'] = active_contracts[c]['Contract ID']
				next_14['Freelancer Name'] = active_contracts[c]['Freelancer Name']
				next_14['End Date'] = active_contracts[c]['End Date'][0:10]
				next_14['Contract Status'] = active_contracts[c]['Status']
				next_14['Expired'] = 'No'
				next_14['Expires Today'] = 'No'

				action_items[c] = next_14

			# Untest contingincies (months with 30 days, February, December)

			# Months with 30 days (April, June, September, November)

			if now.month == 4 or now.month == 6 or now.month == 9 or now.month == 11 and now.day > 16:
				if end_year == now.year and end_month == (now.month +1) and end_day < (now.day + 14 - 30):
					action_items_counter += 1
					next_14['Contract ID'] = active_contracts[c]['Contract ID']
					next_14['Freelancer Name'] = active_contracts[c]['Freelancer Name']
					next_14['End Date'] = active_contracts[c]['End Date'][0:10]
					next_14['Contract Status'] = active_contracts[c]['Status']
					next_14['Expired'] = 'No'
					next_14['Expires Today'] = 'No'

					action_items[c] = next_14

			# February

			elif now.month == 2 and now.day > 15:
				if now.year == 2020 or now.year == 2024:
					if end_year == now.year and end_month == (now.month +1) and end_day < (now.day + 14 - 29):
						action_items_counter += 1
						next_14['Contract ID'] = active_contracts[c]['Contract ID']
						next_14['Freelancer Name'] = active_contracts[c]['Freelancer Name']
						next_14['End Date'] = active_contracts[c]['End Date'][0:10]
						next_14['Contract Status'] = active_contracts[c]['Status']
						next_14['Expired'] = 'No'
						next_14['Expires Today'] = 'No'
				else:
					if end_year == now.year and end_month == (now.month +1) and end_day < (now.day + 14 - 28):
						action_items_counter += 1
						next_14['Contract ID'] = active_contracts[c]['Contract ID']
						next_14['Freelancer Name'] = active_contracts[c]['Freelancer Name']
						next_14['End Date'] = active_contracts[c]['End Date'][0:10]
						next_14['Contract Status'] = active_contracts[c]['Status']
						next_14['Expired'] = 'No'
						next_14['Expires Today'] = 'No'

					action_items[c] = next_14

			#December

			elif now.month == 12 and now.day > 17:
				if end_year == now.year + 1 and end_month == 1 and end_day < (now.day + 14 - 31):
					action_items_counter += 1
					next_14['Contract ID'] = active_contracts[c]['Contract ID']
					next_14['Freelancer Name'] = active_contracts[c]['Freelancer Name']
					next_14['End Date'] = active_contracts[c]['End Date'][0:10]
					next_14['Contract Status'] = active_contracts[c]['Status']
					next_14['Expired'] = 'No'
					next_14['Expires Today'] = 'No'

					action_items[c] = next_14

		output = [['Contract ID','Freelancer Name','End Date']]

		for i in action_items:
			action_item = []
			action_item.append(action_items[i]['Contract ID'])
			action_item.append(action_items[i]['Freelancer Name'])
			action_item.append(action_items[i]['End Date'])
			output.append(action_item)

		return output

	def find_l3_countries(active_contracts):
		action_items = {}
		action_items_counter = 0
		l3_countries_list = ['Australia','Austria','Canada',
								'Denmark','Finland','France',
								'Germany','Ireland','Italy',
								'Liechtenstein','Luxembourg',
								'Monaco','Netherlands','Norway',
								'Portugal','Spain','Sweden','Switzerland',
								'United Kingdom','United States',
								'American Samoa','Guam', 'Puerto Rico',
								'U.S. Virgin Islands',
								'Northern Mariana Islands']

		for c in active_contracts:
			location = active_contracts[c]['Freelancer location'].split(',')
			country = location[0]
	
			if country in l3_countries_list:
				action_items_counter += 1
				action_items[action_items_counter] = active_contracts[c]
 

		output = [['Contract ID','Freelancer Name','Location','Agency']]

		for i in action_items:
			action_item = []
			action_item.append(action_items[i]['Contract ID'])
			action_item.append(action_items[i]['Freelancer Name'])
			action_item.append(action_items[i]['Freelancer location'])
			action_item.append(action_items[i]['Agency Name'])
			output.append(action_item)

		return output

	def gtnp_filter(complete_list):

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

		if len(complete_list) > 0:
			for u in complete_list:
				parts = complete_list[u]['upwork_email'].split('@')
				if len(parts) > 1:
					domain = parts[1]
					if domain != 'upwork.com':
						filtered_counter += 1
						filtered_users[filtered_counter] = complete_list[u]
		else:
			filtered_users[filtered_counter] = 'Empty'

		return filtered_users

	def payroll_filter(complete_list):
		filtered_contracts = {}
		filter_counter = 0
		
		for c in complete_list:
			agency = complete_list[c]['Agency Name']
			if agency != 'Upwork Payroll - iWorkGlobal' and agency != 'EOR-IWG-INTL':
				filter_counter += 1
				filtered_contracts[filter_counter] = complete_list[c]

		return filtered_contracts

	def fixed_price_filter(complete_list):
		filtered_contracts = {}
		filter_counter = 0
		
		for c in complete_list:
			structure = complete_list[c]['Contract type']
			if structure == 'Hourly':
				filter_counter += 1
				filtered_contracts[filter_counter] = complete_list[c]

		return filtered_contracts	


	def find_missing_from_list(list_1, list_2):
		missing_from_list = []
		
		for i in list_2:
			if i not in list_1:
				missing_from_list.append(i)

		return missing_from_list

	def find_common_between_lists(list_1,list_2):
		common_items = []

		for i in list_1:
			if i in list_2:
				common_items.append(i)

		return common_items



	def create_action_list(generator, audit_type):
		file_name = ''

		if audit_type == 1:
			file_name = 'active_users_no_contract'
		if audit_type == 2:
			file_name = 'end_dates'
		if audit_type == 3:
			file_name = 'ICs_in_L3_locations'


		output_path = '/Users/jeffstock/Desktop/' + file_name + '.csv'

		with open(output_path, 'w') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerows(generator)


	def __init__(self, arg):
		super(FileHandler, self).__init__()
		self.arg = arg
		
		


