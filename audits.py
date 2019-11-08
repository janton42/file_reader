#!/usr/bin/env python3
from csv_reader import FileHandler

class Auditor(object):
	"""docstring for Auditor"""

	def l3_locations():

		audit_type = 3

		raw_whitelist = FileHandler.get_raw_whitelist('./static/whitelist.csv')

		l3_countries_list = FileHandler.filter_whitelist(raw_whitelist, 'L3_country')

		l3_contracts_whitelist = FileHandler.filter_whitelist(raw_whitelist, 'Contract')

		contracts_file_name = 'contracts'
		
		active_contracts = FileHandler.fixed_price_filter(FileHandler.payroll_filter(FileHandler.gtnp_filter(FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv'))))

		output = FileHandler.find_hourly_contracts_l3_countries(active_contracts, l3_countries_list, l3_contracts_whitelist)

		FileHandler.create_action_list(output, audit_type)

		print('Audit complete. Type: ICs in L3 Countries')

	def active_users_without_contracts():
		audit_type = 1
		users_file_name = './static/user_data.csv'
		contracts_file_name = './static/contracts.csv'

		auwa = FileHandler.fte_filter(FileHandler.get_active_users(users_file_name))
		active_contracts = FileHandler.gtnp_filter(FileHandler.get_active_contracts(contracts_file_name))

		output = FileHandler.find_users_without_contracts(active_contracts,auwa)

		FileHandler.create_action_list(output, audit_type)

		print('\nAudit complete. Type: Users with systems access, but no contract')

	def end_dates():

		audit_type = 2

		contracts_file_name = 'contracts'

		active_contracts = FileHandler.gtnp_filter(FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv'))

		output = FileHandler.find_end_dates(active_contracts)

		FileHandler.create_action_list(output, audit_type)

		print('Audit complete. Type: End dates')

	def multiple_contracts():

		audit_type = 4

		contracts_file_name = 'contracts'

		active_contracts = FileHandler.gtnp_filter(FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv'))

		output = FileHandler.find_multiple_contracts(active_contracts)

		FileHandler.create_action_list(output, audit_type)

		print('Audit complete. Type: users with multiple contracts')

	def fls_with_assets():

		audit_type = 5

		fl_pc_file_name = 'flr_pc'
		rem_pc_file_name = 'rem_pc'

		fl_mac_file_name = 'fl_mac'
		rem_mac_file_name = 'rem_mac'

		output = 'Yep'

		FileHandler.create_action_list(output, audit_type)

		print('Audit complete. Type: freelancers with Upwork assets\n')

	def __init__(self, arg):
		super(Auditor, self).__init__()
		self.arg = arg
		