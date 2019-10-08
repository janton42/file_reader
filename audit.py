#!/usr/bin/env python3

# from csv_reader import get_active_users, get_audit_users, audit_status_changer


from csv_reader import FileHandler

import datetime

def main():

	output = ''
	now = datetime.datetime.now()
	action_items = {}
	action_items_counter = 0

	file_purpose = input("Is this for an external audit (yes/no)? ")

	if file_purpose == 'yes':
		file_name = 'moss_adams_sample'
		output = FileHandler.get_audit_users('./static/' + file_name + '.csv')
		FileHandler.audit(output)

	elif file_purpose == 'no':
		internal_audit_type = input('What would you like to audit (enter a number)?\n 1 = Active Users with Systems Access\n 2 = Active Contracts\n 3 = End Dates\n ')
		
		if internal_audit_type == '3':

			contracts_file_name = 'contracts'
			needs_action = {}
			active_contracts = FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv')

			for c in active_contracts:

				if active_contracts[c]['End Date'] != '':
					end_year_raw = active_contracts[c]['End Date'][0:4]
					end_year = 0

				if end_year_raw != 'End ':
					end_year = int(end_year_raw)

					# end_month = int(active_contracts[c]['End Date'][5:7])
					# end_day = int(active_contracts[c]['End Date'][8:10])
				else:
					end_year = 1000000000
					end_month = 1000000000
					end_day = 1000000000


				if end_year < now.year:
					needs_action['Contract ID'] = active_contracts[c]['Contract ID']
					needs_action['Freelancer Name'] = active_contracts[c]['Freelancer Name']
					needs_action['Freelancer User ID'] = active_contracts[c]['Freelancer User ID']
					needs_action['End Date'] = active_contracts[c]['End Date']

					action_items_counter += 1
					action_items[action_items_counter] = needs_action

				elif now.month == 12:
					if end_year == now.year + 1 and end_month == 1:
						if now.day >= 16:
							if end_date <= now.day + 14 - 30:
								needs_action['Contract ID'] = active_contracts[c]['Contract ID']
								needs_action['Freelancer Name'] = active_contracts[c]['Freelancer Name']
								needs_action['Freelancer User ID'] = active_contracts[c]['Freelancer User ID']
								needs_action['End Date'] = active_contracts[c]['End Date']

								action_items_counter += 1
								action_items[action_items_counter] = needs_action

				elif end_year == now.year:
					if end_month < now.month:
						needs_action['Contract ID'] = active_contracts[c]['Contract ID']
						needs_action['Freelancer Name'] = active_contracts[c]['Freelancer Name']
						needs_action['Freelancer User ID'] = active_contracts[c]['Freelancer User ID']
						needs_action['End Date'] = active_contracts[c]['End Date']

						action_items_counter += 1
						action_items[action_items_counter] = needs_action

					elif end_month == now.month:
						if end_day < now.day or end_day <= now.day + 14:
							needs_action['Contract ID'] = active_contracts[c]['Contract ID']
							needs_action['Freelancer Name'] = active_contracts[c]['Freelancer Name']
							needs_action['Freelancer User ID'] = active_contracts[c]['Freelancer User ID']
							needs_action['End Date'] = active_contracts[c]['End Date']

							action_items_counter += 1
							action_items[action_items_counter] = needs_action

					elif end_month == now.month + 1:
						if now.month == 4 or now.month == 6 or now.month == 9 or now.month == 11:
							if end_date <= now.day + 14 - 30:
								needs_action['Contract ID'] = active_contracts[c]['Contract ID']
								needs_action['Freelancer Name'] = active_contracts[c]['Freelancer Name']
								needs_action['Freelancer User ID'] = active_contracts[c]['Freelancer User ID']
								needs_action['End Date'] = active_contracts[c]['End Date']

								action_items_counter += 1
								action_items[action_items_counter] = needs_action

						elif now.month == 2:
							if end_date <= now.day + 14 - 28:
								needs_action['Contract ID'] = active_contracts[c]['Contract ID']
								needs_action['Freelancer Name'] = active_contracts[c]['Freelancer Name']
								needs_action['Freelancer User ID'] = active_contracts[c]['Freelancer User ID']
								needs_action['End Date'] = active_contracts[c]['End Date']

								action_items_counter += 1
								action_items[action_items_counter] = needs_action
						else:
							if end_date <= now.day + 14 -31:
								needs_action['Contract ID'] = active_contracts[c]['Contract ID']
								needs_action['Freelancer Name'] = active_contracts[c]['Freelancer Name']
								needs_action['Freelancer User ID'] = active_contracts[c]['Freelancer User ID']
								needs_action['End Date'] = active_contracts[c]['End Date']

								action_items_counter += 1
								action_items[action_items_counter] = needs_action

			print(action_items)
		else:
			print('None')



		# active_users = FileHandler.get_active_users('./static/' + users_file_name + '.csv')
		# print('There are ', len(active_users), 'TIP users with systems access')
		# print('There are ', len(active_contrac), 'TIP users with systems access')

	else:
		print('Please enter "yes" or "no" (case sensitive).')
		main()
		
	continue_audits = input('Would you like to run another audit (yes/no)? ')

	if continue_audits == 'yes':
		main()
	elif continue_audits == 'no':
		print('Goodbye!','\n','\n')
	else:
		print('Response invalid - starting over')
		main()

	

if __name__ == '__main__':
	main()


