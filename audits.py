#!/usr/bin/env python3
from csv_reader import *

class Auditor:
	"""docstring for Auditor"""
	e = './static/ended_contracts.csv'
	a = './static/contracts.csv'
	u = './static/user_data.csv'
	w = './static/whitelist.csv'
	rmac = './static/rem_mac.csv'
	flmac = './static/flr_mac.csv'
	flpc = './static/flr_pc.csv'
	mpc = './static/rem_pc.csv'
	cc = './static/cost_centers.csv'
	
	ended_contracts = ListHandler.gtnp_filter(Getters.get_contracts(e))
	active_contracts = ListHandler.gtnp_filter(Getters.get_contracts(a))
	auwa = ListHandler.fte_filter_user_list(Getters.get_active_users(u))
	whitelist = Getters.get_raw_whitelist(w)
	cc_list = Getters.get_raw_whitelist(cc)

	complete_mac_list = Finders.find_location_and_agency(Finders.find_fl_with_mac_assets(ListHandler.fte_filter_mac_assets(Getters.get_users_with_mac_assets(rmac, flmac)), auwa), active_contracts)
	complete_pc_list = Finders.find_location_and_agency(Finders.find_fl_with_pc_assets(Getters.get_users_with_pc_assets(flpc, mpc), auwa), active_contracts)

	contracts_whitelist = ListHandler.filter_whitelist(whitelist, 'Contract')
	countries_whitelist = ListHandler.filter_whitelist(whitelist, 'L3_country')

	def active_users_without_contracts():
		audit_type = 1
		users = Finders.find_users_without_contracts(Auditor.active_contracts, Auditor.auwa)

		FileHandler.create_action_list(users, audit_type)
		print('\nAudit complete. Type: Users with systems access, but no contract')

	def end_dates():
		audit_type = 2
		contracts_list = Finders.find_end_dates(Auditor.active_contracts)

		FileHandler.create_action_list(contracts_list, audit_type)
		print('Audit complete. Type: End dates')

	def l3_locations():
		audit_type = 3
		filtered_contracts = ListHandler.fixed_price_filter(ListHandler.payroll_filter(Auditor.active_contracts))
		contracts_list = Finders.find_hourly_contracts_l3_countries(filtered_contracts, Auditor.countries_whitelist, Auditor.contracts_whitelist)

		FileHandler.create_action_list(contracts_list, audit_type)
		print('Audit complete. Type: ICs in L3 Countries')

	def multiple_contracts():
		audit_type = 4
		contracts_list = Finders.find_multiple_contracts(Auditor.active_contracts)

		FileHandler.create_action_list(contracts_list, audit_type)
		print('Audit complete. Type: users with multiple contracts')

	def fls_with_assets():
		audit_type = 5
		users = ListHandler.remove_duplicates_from_nested_list(ListHandler.list_combiner(Auditor.complete_mac_list, Auditor.complete_pc_list))

		FileHandler.create_action_list(users, audit_type)
		print('Audit complete. Type: freelancers with Upwork assets')

	def currently_whitelisted():
		audit_type = 6
		current_list = WhitelistUpdater.current_whitelist(Auditor.active_contracts, Auditor.contracts_whitelist)

		FileHandler.create_action_list(current_list, audit_type)

		audit_type = 7
		updated_list = WhitelistUpdater.update(Auditor.ended_contracts, Auditor.contracts_whitelist, Auditor.whitelist)
		FileHandler.create_action_list(updated_list ,audit_type)

		print('Audit complete. Type: Currently Whitelisted')

	def survey_prep():
		audit_type = 8

		survey = SurveyPreper.prepare(Auditor.active_contracts, Auditor.auwa, Auditor.cc_list)

		FileHandler.create_action_list(survey, audit_type)
		print('Survey Prep Complete.\n')


	def __init__(self, arg):
		super(Auditor, self).__init__()
		self.arg = arg
		
		