#!/usr/bin/env python3

# from csv_reader import get_active_users, get_audit_users, audit_status_changer


from csv_reader import FileHandler

import datetime

def main():

	output = ''
	now = datetime.datetime.now()
	

	file_purpose = input("Is this for an external audit (yes/no)? ")

	if file_purpose == 'yes':
		file_name = 'moss_adams_sample'
		output = FileHandler.get_audit_users('./static/' + file_name + '.csv')
		FileHandler.audit(output)

	elif file_purpose == 'no':
		internal_audit_type = input('What would you like to audit (enter a number)?\n 1 = Active Users with Systems Access\n 2 = Active Contracts\n 3 = End Dates\n ')
		if internal_audit_type == '1':
			users_file_name = 'user_data'
			contracts_file_name = 'contracts'
			auwa = FileHandler.fte_filter(FileHandler.get_active_users('./static/' + users_file_name + '.csv'))
			active_contracts = FileHandler.team_filter(FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv'))
			
			print('There are ', len(auwa), ' active users with access.\n')
			print('There are ', len(active_contracts), ' active contracts')
			
			print(auwa[1])
			contracts_and_users = {}
			contracts_and_users_counter = 0
			for u in auwa:	
				for c in active_contracts:
					if auwa[u]['worker_user_id'] in active_contracts[c].values():
						contracts_and_users_counter += 1
						contracts_and_users[contracts_and_users_counter] = active_contracts[c]

			print(len(contracts_and_users))
			# print('jesse-ratner' in auwa[1].values())
			# compared = FileHandler.uid_compare(active_contracts, auwa)
			
			# return(len(compared))



		elif internal_audit_type == '2':

			contracts_file_name = 'contracts'

			active_contracts = FileHandler.team_filter(FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv'))

			tip_contracts = FileHandler.team_filter(active_contracts)

			print('There are ', len(tip_contracts), ' active TIP contracts.\n')
			# print(len(active_contracts))
			
			# for i in active_contracts:
			# 	print(active_contracts[i]['Contract ID'], active_contracts[i]['Freelancer Name'], tip_contracts[i]['Team Name'])

		elif internal_audit_type == '3':

			contracts_file_name = 'contracts'
			action_items = {}
			action_items_counter = 0
			now = datetime.datetime.now()

			date = now.strftime('%Y/%m/%d')

			active_contracts = FileHandler.team_filter(FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv'))

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


			# Output

			print('There are ', len(active_contracts), ' active contracts.\n')
			if len(action_items) == 1:
				print('There is 1 action item.\n')
			else:
				print('There are ', len(action_items), ' action items.\n')
			total_expired = 0
			total_expiring_today = 0
			total_expiring_next_14 = 0

			for item in action_items:
				if action_items[item]['Expired'] == 'Yes':
					total_expired += 1
				if action_items[item]['Expires Today'] == 'Yes':
					total_expiring_today += 1
				if action_items[item]['Expired'] == 'No' and action_items[item]['Expires Today'] == 'No':
					total_expiring_next_14 += 1

			if total_expired == 1:
				print(total_expired, ' contract is expired.\n')
			else:
				print(total_expired, ' contracts are expired.\n' )

			for item in action_items:
				if action_items[item]['Expired'] == 'Yes':
					print(action_items[item]['Contract ID'], action_items[item]['Freelancer Name'], action_items[item]['End Date'])
			print()

			if total_expiring_today == 1:
				print(total_expiring_today, ' contract is expiring today.\n')
			else:
				print(total_expiring_today, ' contracts are expiring today.\n' )

			for item in action_items:
				if action_items[item]['Expires Today'] == 'Yes':
					print(action_items[item]['Contract ID'], action_items[item]['Freelancer Name'], action_items[item]['End Date'])
			print()

			if total_expiring_next_14 == 1:
				print('1 contract is expiring in the next 14 days.\n')
			else:
				print(total_expiring_next_14, ' contracts are expiring in the next 14 days.\n')


			for item in action_items:
				if action_items[item]['Expires Today'] == 'No' and action_items[item]['Expired'] == 'No':
					print(action_items[item]['Contract ID'], action_items[item]['Freelancer Name'], action_items[item]['End Date'])
			print()

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


