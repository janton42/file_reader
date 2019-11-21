#!/usr/bin/env python3
from csv_reader import *

class Auditor(object):
	"""docstring for Auditor"""

	def l3_locations():

		audit_type = 3

		raw_whitelist = Getters.get_raw_whitelist('./static/whitelist.csv')

		l3_countries_list = ListHandler.filter_whitelist(raw_whitelist, 'L3_country')

		l3_contracts_whitelist = ListHandler.filter_whitelist(raw_whitelist, 'Contract')

		contracts_file_name = 'contracts'
		
		active_contracts = ListHandler.fixed_price_filter(ListHandler.payroll_filter(ListHandler.gtnp_filter(Getters.get_contracts('./static/' + contracts_file_name + '.csv'))))

		output = FileHandler.find_hourly_contracts_l3_countries(active_contracts, l3_countries_list, l3_contracts_whitelist)

		FileHandler.create_action_list(output, audit_type)

		print('Audit complete. Type: ICs in L3 Countries')

	def active_users_without_contracts():
		audit_type = 1
		users_file_name = './static/user_data.csv'
		contracts_file_name = './static/contracts.csv'

		auwa = ListHandler.fte_filter_user_list(Getters.get_active_users(users_file_name))
		active_contracts = ListHandler.gtnp_filter(Getters.get_contracts(contracts_file_name))

		output = FileHandler.find_users_without_contracts(active_contracts,auwa)

		FileHandler.create_action_list(output, audit_type)

		print('\nAudit complete. Type: Users with systems access, but no contract')

	def end_dates():

		audit_type = 2

		contracts_file_name = 'contracts'

		active_contracts = ListHandler.gtnp_filter(Getters.get_contracts('./static/' + contracts_file_name + '.csv'))

		output = FileHandler.find_end_dates(active_contracts)

		FileHandler.create_action_list(output, audit_type)

		print('Audit complete. Type: End dates')

	def multiple_contracts():

		audit_type = 4

		contracts_file_name = 'contracts'

		active_contracts = ListHandler.gtnp_filter(Getters.get_contracts('./static/' + contracts_file_name + '.csv'))

		output = FileHandler.find_multiple_contracts(active_contracts)

		FileHandler.create_action_list(output, audit_type)

		print('Audit complete. Type: users with multiple contracts')

	def fls_with_assets():

		audit_type = 5

		fl_pc = './static/flr_pc.csv'
		rem_pc = './static/rem_pc.csv'
		fl_mac = './static/flr_mac.csv'
		rem_mac = './static/rem_mac.csv'
		users_file_name = './static/user_data.csv'
		active_contracts_file_name = './static/contracts.csv'
		ended_contracts_file_name = './static/ended_contracts.csv'

		auwa = ListHandler.fte_filter_user_list(Getters.get_active_users(users_file_name))
		active_contracts = ListHandler.gtnp_filter(Getters.get_contracts(active_contracts_file_name))

		ended_contracts = ListHandler.gtnp_filter(Getters.get_contracts(ended_contracts_file_name))

		combined_mac_list = ListHandler.fte_filter_mac_assets(Getters.get_users_with_mac_assets(rem_mac, fl_mac))

		complete_mac_list = FileHandler.find_location_and_agency(FileHandler.find_fl_with_mac_assets(combined_mac_list, auwa), active_contracts)

		complete_pc_list = FileHandler.find_location_and_agency(FileHandler.find_fl_with_pc_assets(Getters.get_users_with_pc_assets(fl_pc, rem_pc), auwa), active_contracts)

		output = ListHandler.remove_duplicates_from_nested_list(ListHandler.list_combiner(complete_mac_list, complete_pc_list))

		FileHandler.create_action_list(output, audit_type)

		print('Audit complete. Type: freelancers with Upwork assets\n')

	def __init__(self, arg):
		super(Auditor, self).__init__()
		self.arg = arg
		
		