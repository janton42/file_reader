#!/usr/bin/env python3
from csv_reader import *

class Auditor(object):
	"""docstring for Auditor"""

	ended_contracts = ListHandler.gtnp_filter(Getters.get_contracts('./static/ended_contracts.csv'))
	active_contracts = ListHandler.gtnp_filter(Getters.get_contracts('./static/contracts.csv'))
	auwa = ListHandler.fte_filter_user_list(Getters.get_active_users('./static/user_data.csv'))
	whitelist = Getters.get_raw_whitelist('./static/whitelist.csv')
	contracts_whitelist = ListHandler.filter_whitelist(whitelist, 'Contract')
	countries_whitelist = ListHandler.filter_whitelist(whitelist, 'L3_country')
	complete_mac_list = Finders.find_location_and_agency(Finders.find_fl_with_mac_assets(ListHandler.fte_filter_mac_assets(Getters.get_users_with_mac_assets('./static/rem_mac.csv', './static/flr_mac.csv')), Auditor.auwa), Auditor.active_contracts)
	complete_pc_list = Finders.find_location_and_agency(Finders.find_fl_with_pc_assets(Getters.get_users_with_pc_assets('./static/flr_pc.csv', './static/rem_pc.csv'), Auditor.auwa), Auditor.active_contracts)


	def l3_locations():
		audit_type = 3
		filtered_contracts = ListHandler.fixed_price_filter(ListHandler.payroll_filter(Auditor.active_contracts))
		output = Finders.find_hourly_contracts_l3_countries(filtered_contracts, Auditor.countries_whitelist, Auditor.contracts_whitelist)
		FileHandler.create_action_list(output, audit_type)
		print('Audit complete. Type: ICs in L3 Countries')

	def active_users_without_contracts():
		audit_type = 1
		output = Finders.find_users_without_contracts(Auditor.active_contracts, Auditor.auwa)
		FileHandler.create_action_list(output, audit_type)
		print('\nAudit complete. Type: Users with systems access, but no contract')

	def end_dates():
		audit_type = 2
		output = Finders.find_end_dates(Auditor.active_contracts)
		FileHandler.create_action_list(output, audit_type)
		print('Audit complete. Type: End dates')

	def multiple_contracts():
		audit_type = 4
		output = Finders.find_multiple_contracts(Auditor.active_contracts)
		FileHandler.create_action_list(output, audit_type)
		print('Audit complete. Type: users with multiple contracts')

	def fls_with_assets():
		audit_type = 5
		output = ListHandler.remove_duplicates_from_nested_list(ListHandler.list_combiner(Auditor.complete_mac_list, Auditor.complete_pc_list))
		FileHandler.create_action_list(output, audit_type)
		print('Audit complete. Type: freelancers with Upwork assets')

	def currently_whitelisted():
		audit_type = 6
		FileHandler.create_action_list(WhitelistUpdater.current_whitelist(Auditor.active_contracts, Auditor.contracts_whitelist), audit_type)
		print('Audit complete. Type: Currently Whitelisted\n')
		audit_type = 7
		FileHandler.create_action_list(WhitelistUpdater.update(Auditor.ended_contracts, Auditor.contracts_whitelist, Auditor.whitelist),audit_type)

	def __init__(self, arg):
		super(Auditor, self).__init__()
		self.arg = arg
		
		