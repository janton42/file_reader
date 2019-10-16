#!/usr/bin/env python3

# from csv_reader import get_active_users, get_audit_users, audit_status_changer


from csv_reader import FileHandler

# from emailer import Emailer



def main():

	output = ''
	
	

	file_purpose = input("Is this for an external audit (yes/no)? ")

	if file_purpose == 'yes':
		file_name = 'moss_adams_sample'
		output = FileHandler.get_audit_users('./static/' + file_name + '.csv')
		FileHandler.audit(output)

	elif file_purpose == 'no':
		internal_audit_type = input('What would you like to audit (enter a number)?\n 1 = Active Users with Systems Access\n 2 = Active Contracts\n 3 = End Dates\n ')
		
		if internal_audit_type == '1':
			
			users_file_name = './static/user_data.csv'
			contracts_file_name = './static/contracts.csv'

			auwa = FileHandler.fte_filter(FileHandler.get_active_users(users_file_name))
			active_contracts = FileHandler.team_filter(FileHandler.get_active_contracts(contracts_file_name))

			output = FileHandler.find_users_without_contracts(active_contracts,auwa)

			print(output)
			

			FileHandler.create_action_list(output)

			continue_audits = input('Would you like to run another audit (yes/no)? ')

			# FileHandler.user_interface(continue_audits)

			if continue_audits == 'yes':
				main()
			elif continue_audits == 'no':
				print('Goodbye!','\n','\n')
			else:
				print('Response invalid - starting over')
				main()

		elif internal_audit_type == '2':

			contracts_file_name = 'contracts'

			active_contracts = FileHandler.team_filter(FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv'))

			tip_contracts = FileHandler.team_filter(active_contracts)

			print('There are ', len(tip_contracts), ' active TIP contracts.\n')

			continue_audits = input('Would you like to run another audit (yes/no)? ')

			if continue_audits == 'yes':
				main()
			elif continue_audits == 'no':
				print('Goodbye!','\n','\n')
			else:
				print('Response invalid - starting over')
				main()
			
		elif internal_audit_type == '3':

			contracts_file_name = 'contracts'

			active_contracts = FileHandler.team_filter(FileHandler.get_active_contracts('./static/' + contracts_file_name + '.csv'))

			output = FileHandler.find_end_dates(active_contracts)

			print(output)

			FileHandler.create_action_list(output)

			continue_audits = input('Would you like to run another audit (yes/no)? ')

			if continue_audits == 'yes':
				main()
			elif continue_audits == 'no':
				print('Goodbye!','\n','\n')
			else:
				print('Response invalid - starting over')
				main()

		else:
			print('None')
	else:
		print('Please enter "yes" or "no" (case sensitive).')
		main()
		

	

if __name__ == '__main__':
	main()


