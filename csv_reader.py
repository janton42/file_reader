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

	def create_dict(file_location):
		compiled_list = csv.reader(open(file_location, 'r'))

		dict_list = {}
		key = 0
		
		for v in compiled_list:
		   dict_list[key] = v
		   key += 1

		return dict_list

	def create_action_list(generator, audit_type):
		file_name = ''

		if audit_type == 1:
			file_name = 'active_users_no_contract'
		elif audit_type == 2:
			file_name = 'end_dates'
		elif audit_type == 3:
			file_name = 'ICs_in_L3_locations'
		elif audit_type == 4:
			file_name = 'multiple_contracts'
		elif audit_type == 5:
			file_name = 'fls_with_assets'
		elif audit_type == 6:
			file_name = 'current_whitelist'
		elif audit_type == 7:
			file_name = 'updated_whitlist'
		elif audit_type == 'adhoc':
			file_name = input("Please enter an output file name: ").strip()


		output_path = '/Users/jeffstock/Desktop/' + file_name + '.csv'

		with open(output_path, 'w') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerows(generator)

	def __init__(self, arg):
		super(FileHandler, self).__init__()
		self.arg = arg

class Getters(object):
	"""docstring for Getters"""

	def get_users_with_mac_assets(rem, fl):

		rem_dict = FileHandler.create_dict(rem)
		fl_dict = FileHandler.create_dict(fl)

		combined_pc = DictHandler.dict_combiner(rem_dict, fl_dict)

		a = {}
		b = 0

		all_data = {}
		user_detail_counter = 0

		for user in combined_pc:

			user_details = {}

			ind_user_detail = combined_pc.get(user)

			user_details['User Details'] = ind_user_detail

			user_detail_counter += 1

			all_data[user_detail_counter] = user_details
		
		headers = all_data[1]['User Details']

		for data in all_data:
			pair = {}
			i = 0
			tester = all_data[data]['User Details']

			while i < len(headers):
				k = headers[i]
				v = tester[i]
				i += 1
				pair[k] = v
			b += 1
			a[b] = pair

		return a

	def get_users_with_pc_assets(rem, fl):
		output = []
		combined_list = []
		long_desc = []
		rough_list = []

		rem_dict = FileHandler.create_dict(rem)
		fl_dict = FileHandler.create_dict(fl)

		for i in rem_dict:
			test = rem_dict[i][len(rem_dict[i])-1]
			combined_list.append(test)

		for a in fl_dict:
			test = fl_dict[a][len(fl_dict[a])-1]
			combined_list.append(test)

		for b in combined_list:
			parts_1 = b.split(',')
			parts_2 = b.split('-')
			if len(parts_1) > 1:
				long_desc.append(parts_1)
			elif len(parts_2) > 2:
				long_desc.append(parts_2)
			else:
				rough_list.append(b)

		for c in long_desc:
			name = c[0].strip()
			rough_list.append(name)

		for d in rough_list:
			if d != '-' and d != 'Description':
				output.append(d)

		return output

	def get_active_users(file_location):
	
		user_list = FileHandler.create_dict(file_location)

		a = {}
		b = 0

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

	def get_contracts(file_location):

		# complete_list = {}
		# complete_list_counter = 0

		contract_list = FileHandler.create_dict(file_location)

		headers = contract_list[0]

		a = {}
		b = 0
		

		for data in contract_list:
			pair = {}
			i = 1
			tester = contract_list[data]

			while i < len(tester):
				k = headers[i-1]
				v = tester[i-1]
				i += 1
				pair[k] = v
			b += 1
			a[b] = pair


		return a

	def get_raw_whitelist(file_location):
		info_list = FileHandler.create_dict(file_location)

		headers = info_list[0]

		a = {}
		b = 0
		

		for data in info_list:
			pair = {}
			i = 0
			tester = {}
			if data != 0:
				tester = info_list[data]
			
			if len(tester) > 0:
				while i < len(tester):
					k = headers[i]
					v = tester[i]
					i += 1
					pair[k] = v
				b += 1
				a[b] = pair


		return a

	def __init__(self, arg):
		super(Getters, self).__init__()
		self.arg = arg

class Finders(object):
	"""docstring for Finders"""
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

		filtered_by_uid = ListHandler.find_missing_from_list(uids_contracts,uids_users)
		filtered_by_name = ListHandler.find_missing_from_list(names_contracts,names_users)

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
			if end_year == now.year -1 or end_year == now.year -2 or end_year == now.year and end_month == now.month and end_day < now.day or end_year == now.year and end_month < now.month:
				
				expired = DictHandler.create_end_date_dict(active_contracts[c])

				action_items[c] = expired

			# Contracts ending today
			elif end_year == now.year and end_month == now.month and end_day == now.day:
				
				expires_today = DictHandler.create_end_date_dict(active_contracts[c])

				action_items[c] = expires_today

			# Contracts expiring this month within the next 14 days
			elif end_year == now.year and end_month == now.month and end_day > now.day and end_day <= (now.day + 14):
				action_items_counter += 1
				next_14 = DictHandler.create_end_date_dict(active_contracts[c])

				action_items[c] = next_14

			# Contracts expiring next month when end dates are within 14 days of today
			if now.day > 17:

				#December
				if now.month == 12:
					if end_year == now.year + 1 and end_month == 1 and end_day < (now.day + 14 - 31):

						next_14 = DictHandler.create_end_date_dict(active_contracts[c])

						action_items[c] = next_14

				#February
				elif now.month == 2:
					if now.year == 2020 or now.year == 2024:
						if end_year == now.year and end_month == (now.month +1) and end_day < (now.day + 14 - 29):
						
							next_14 = DictHandler.create_end_date_dict(active_contracts[c])
					else:
						if end_year == now.year and end_month == (now.month +1) and end_day < (now.day + 14 - 28):

							next_14 = DictHandler.create_end_date_dict(active_contracts[c])

						action_items[c] = next_14

				# Months with 30 days (April, June, September, November)
				# TODO
				# USE THIS FOR TESTING
				elif now.month == 4 or now.month == 6 or now.month == 9 or now.month == 11:
					if end_year == now.year and end_month == (now.month +1) and end_day < (now.day + 14 - 30):

						next_14 = DictHandler.create_end_date_dict(active_contracts[c])

						action_items[c] = next_14

				# TEST ABOVE

				# Contracts expiring this month within the next 14 days
				elif end_year == now.year and end_month == now.month and end_day > now.day and end_day <= (now.day + 14):
					action_items_counter += 1

					next_14 = DictHandler.create_end_date_dict(active_contracts[c])

					action_items[c] = next_14

				# Contracts expiring next month within 14 days for months with 31 days and end_day == (now.day + 14 - 31)
				if end_year == now.year and end_month == (now.month + 1) and end_day <= now.day + 14 - 31:

					next_14 = DictHandler.create_end_date_dict(active_contracts[c])

					action_items[c] = next_14

			elif now.day > 16:
				if now.month == 2:
					if now.year == 2020 or now.year == 2024:
						if end_year == now.year and end_month == (now.month +1) and end_day < (now.day + 14 - 29):
							
							next_14 = DictHandler.create_end_date_dict(active_contracts[c])
					else:
						if end_year == now.year and end_month == (now.month +1) and end_day < (now.day + 14 - 28):

							next_14 = DictHandler.create_end_date_dict(active_contracts[c])

						action_items[c] = next_14

				# Months with 30 days (April, June, September, November)

				elif now.month == 4 or now.month == 6 or now.month == 9 or now.month == 11:
					if end_year == now.year and end_month == (now.month +1) and end_day <= (now.day + 14 - 30):

						next_14 = DictHandler.create_end_date_dict(active_contracts[c])

						action_items[c] = next_14
				
				elif end_year == now.year and end_month == now.month and end_day > now.day and end_day <= (now.day + 14):

					next_14 = DictHandler.create_end_date_dict(active_contracts[c])

					action_items[c] = next_14

				# Contracts ending this month in the next 14 days (starting tomorrow)

		output = [['Contract ID','User ID','Freelancer Name','Contact Person','Team Name','End Date','Payment Structure']]

		for i in action_items:
			action_item = []
			action_item.append(action_items[i]['Contract ID'])
			action_item.append(action_items[i]['User ID'])
			action_item.append(action_items[i]['Freelancer Name'])
			action_item.append(action_items[i]['Contact Person'])
			action_item.append(action_items[i]['Team Name'])
			action_item.append(action_items[i]['End Date'])
			action_item.append(action_items[i]['Contract Type'])
			output.append(action_item)

		return output

	def find_hourly_contracts_l3_countries(active_contracts, l3_countries_list, whitelist):
		action_items = {}
		action_items_counter = 0

		for c in active_contracts:
			freelancer_name = active_contracts[c]['Freelancer Name']
			access = active_contracts[c]['Systems Access']
			contract_id = active_contracts[c]['Contract ID']
			if contract_id not in whitelist and freelancer_name != 'Upwork Managed Services' and freelancer_name != 'Professionals Agency P' and access != 'Domestic Staffing Vendor Employee':
				location = active_contracts[c]['Freelancer location'].split(',')
				country = location[0]
				if country in l3_countries_list:
					action_items_counter += 1
					action_items[action_items_counter] = active_contracts[c]
 

		output = [['Contract ID','Freelancer Name','Location','Agency','Weekly Limit','Contact Person','Contract End Date','Notes']]

		for i in action_items:
			action_item = []
			
			action_item.append(action_items[i]['Contract ID'])
			action_item.append(action_items[i]['Freelancer Name'])
			action_item.append(action_items[i]['Freelancer location'])
			action_item.append(action_items[i]['Agency Name'])
			action_item.append(action_items[i]['Weekly Limit'])
			action_item.append(action_items[i]['Contact person'])
			action_item.append(action_items[i]['End Date'][0:10])
			
			# if contract_id in whitelist:
			# 	action_item.append('Yes')
			# else:
			# 	action_item.append('No')
			output.append(action_item)

		return output

	def find_fl_with_mac_assets(email_list, access_dict):
		output = {}
		counter = 0

		for i in access_dict:
			single = {}
			full_name = access_dict[i]['full_name']
			email = access_dict[i]['upwork_email']
			uid = access_dict[i]['worker_user_id']

			for k in email_list:
				if email in k:
					counter += 1
					single['Full Name'] = full_name
					single['User ID'] = uid
					single['Email Address'] = email

					output[counter] = single
		
		return output

	def find_fl_with_pc_assets(names_list, access_dict):
		output = {}
		counter = 0

		for i in access_dict:
			single = {}
			full_name = access_dict[i]['full_name']
			email = access_dict[i]['upwork_email']
			uid = access_dict[i]['worker_user_id']

			for a in names_list:
				if full_name == a:
					counter += 1
					single['Full Name'] = full_name
					single['User ID'] = uid
					single['Email Address'] = email

					output[counter] = single

		return output

	def find_location_and_agency(user_dict, contract_dict):
		output = [['Full Name','User ID','Email Address','Agency Name','Location']]

		for c in contract_dict:
			single = []
			for u in user_dict:
				if user_dict[u]['User ID'] == contract_dict[c]['Freelancer User ID']:
					single.append(user_dict[u]['Full Name'])
					single.append(user_dict[u]['User ID'])
					single.append(user_dict[u]['Email Address'])
					single.append(contract_dict[c]['Agency Name'])
					single.append(contract_dict[c]['Freelancer location'])

					output.append(single)

		return output

	def find_multiple_contracts(active_contracts):

		output = [['Contract ID','User ID','Freelancer Name','Contact Person','Team Name','End Date']]
		uids_all = []
		repeats = []
		for i in active_contracts:
			uid = active_contracts[i]['Freelancer User ID']
			if uid != 'odesk_managed':
				uids_all.append(uid)

		for c in active_contracts:
			uid = active_contracts[c]['Freelancer User ID']
			x = uids_all.count(uid)
			if x > 1 and uid not in repeats:
				repeats.append(uid)

		for a in active_contracts:
			action_item = []
			uid = active_contracts[a]['Freelancer User ID']
			if uid in repeats:
				action_item.append(active_contracts[a]['Contract ID'])
				action_item.append(active_contracts[a]['Freelancer User ID'])
				action_item.append(active_contracts[a]['Freelancer Name'])
				action_item.append(active_contracts[a]['Contact person'])
				action_item.append(active_contracts[a]['Team Name'])
				action_item.append(active_contracts[a]['End Date'][0:10])
				output.append(action_item)

		return output

	def __init__(self, arg):
		super(Finders, self).__init__()
		self.arg = arg
				
class ListHandler(object):
	"""docstring for ListHandler"""

	def list_combiner(base, additional):

		for i in additional:
			if i not in base:
				base.append(i)

		return base

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

	def fte_filter_mac_assets(user_list):
		email_address_list = []

		fl_with_assets = {}
		counter = 0

		for u in user_list:
			domain = user_list[u]['Username'].split('@')
			email = user_list[u]['Username']
			if len(domain) > 1 and domain[1] == 'cloud.upwork.com':
				counter += 1
				fl_with_assets[counter] = email

		output = []

		for i in fl_with_assets:
			single = []

			single.append(fl_with_assets[i])

			output.append(single)

		return output

	def fte_filter_user_list(complete_list):
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

	def remove_duplicates_from_nested_list(nested_list):
		output = []
		tester = []

		for i in nested_list:
			name = i[0]
			if name not in tester:
				tester.append(name)
				output.append(i)

		return output

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

	def filter_whitelist(whitelist, list_type):
		filtered_list = []

		for i in whitelist:
			if whitelist[i]['Type'] == list_type:
				filtered_list.append(whitelist[i]['Name'])

		return filtered_list
	
	def __init__(self, arg):
		super(ListHandler, self).__init__()
		self.arg = arg

class DictHandler(object):
	"""docstring for DictHandler"""
	
	def dict_combiner(base, additional):

		key = len(base) + 1

		for i in additional:
			base[key] = additional[i]
			key += 1

		return base

	def create_end_date_dict(base_item):
		output = {}

		output['Contract ID'] = base_item['Contract ID']
		output['Freelancer Name'] = base_item['Freelancer Name']
		output['End Date'] = base_item['End Date'][0:10]
		output['Contract Status'] = base_item['Status']
		output['User ID'] = base_item['Freelancer User ID']
		output['Team Name'] = base_item['Team Name']
		output['Contact Person'] = base_item['Contact person']
		output['Contract Type'] = base_item['Contract type']

		return output

	def __init__(self, arg):
		super(DictHandler, self).__init__()
		self.arg = arg

class WhitelistUpdater(object):
	"""docstring for WhitelistUpdater"""
	def current_whitelist(details, ended, contracts):

		current = [['Contract ID','Offer ID','Company Name','Team Name','Freelancer User ID','Freelancer Name','Freelancer location','Agency Name','Title','Start Date','End Date','Status','Hourly Rate','Fixed Price Amount Agreed','Upfront Payment (%)','Weekly Salary','Weekly Limit','Contact person','Contract type','Milestone Status','Escrow Refund Status','Cost Center','Division','Systems Access','Geographic Zone','Level','Job Category','Imperative Team','isBYO']]
		

		for i in details:
			cid = details[i]['Contract ID']
			if cid in contracts:
				single = []
				for c in details[i]:
					single.append(details[i][c])
				current.append(single)

		return current

	def update(ended, contracts, whitelist):
		updated = [['Type','Name']]

		closed = []

		for a in ended:
			cid = ended[a]['Contract ID']
			if cid in contracts:
				closed.append(cid)

		return updated


	def __init__(self, arg):
		super(WhitelistUpdater, self).__init__()
		self.arg = arg
		

class Adhoc(object):
	"""docstring for Adhoc"""

	c = ListHandler.gtnp_filter(Getters.get_contracts('./static/contracts.csv'))
	e = Getters.get_contracts('./static/ended_contracts.csv')

	def report_maker(i):
		
		output.append(i)

		return output

	def team_filter(contract_dict):

		team = input('Please enter a team name: ').strip()
		output = [['Contract ID','Offer ID','Company Name','Team Name','Freelancer User ID','Freelancer Name','Freelancer location','Agency Name','Title','Start Date','End Date','Status','Hourly Rate','Fixed Price Amount Agreed','Upfront Payment (%)','Weekly Salary','Weekly Limit','Contact person','Contract type','Milestone Status','Escrow Refund Status','Cost Center','Division','Systems Access','Geographic Zone','Level','Job Category','Imperative Team','isBYO']]

		for c in contract_dict:
			i = contract_dict[c]
			t = i['Team Name']
			if t == team:
				single = []
				for a in i:
					single.append(i[a])
				output.append(single)

		FileHandler.create_action_list(output,'adhoc')

	def contract_starts_by_year(contract_dict):

		year_filter = input('Please enter a four-digit year: ').strip()
		output = [['Contract ID','Offer ID','Company Name','Team Name','Freelancer User ID','Freelancer Name','Freelancer location','Agency Name','Title','Start Date','End Date','Status','Hourly Rate','Fixed Price Amount Agreed','Upfront Payment (%)','Weekly Salary','Weekly Limit','Contact person','Contract type','Milestone Status','Escrow Refund Status','Cost Center','Division','Systems Access','Geographic Zone','Level','Job Category','Imperative Team','isBYO']]

		filter_results = []

		out = []

		older = []

		for c in contract_dict:
			i = contract_dict[c]
			start_date = i['Start Date'].split('-')[0]
			if start_date == year_filter:
				filter_results.append(i['Freelancer User ID'])
			elif start_date < year_filter:
				older.append(i['Freelancer User ID'])

		p_users = Adhoc.create_filter_list(Adhoc.e,'Freelancer User ID')

		current_older = []

		for x in filter_results:
			if x in older:
				current_older.append(x)

		for a in filter_results:
			if a not in p_users and a not in older:
				out.append(a)

		for b in contract_dict:
			i = contract_dict[b]
			u = i['Freelancer User ID']
			if u in out:
				single = []
				for a in i:
					single.append(i[a])
				output.append(single)

		FileHandler.create_action_list(output,'adhoc')

	def create_filter_list(dictionary, parameter):
		output = []

		for i in dictionary:
			searched = dictionary[i][parameter]
			if searched not in output:
				output.append(searched)

		return output

	def find_team_from_fl_name(name_list):

		output = [['Timestamp','Nominee Name','Nominee Start Date','Nomination Details','Nominated by Email','Team']]

		names = FileHandler.create_dict(name_list)

		for a in Adhoc.c:
			c_name = Adhoc.c[a]['Freelancer Name']
			for b in names:
				nom_name = names[b][1]
				if c_name == nom_name:
					names[b].append(Adhoc.c[a]['Team Name'].split('::')[0])
					output.append(names[b])

		FileHandler.create_action_list(output,'adhoc')

		return output

	def __init__(self, arg):
		super(Adhoc, self).__init__()
		self.arg = arg
		

