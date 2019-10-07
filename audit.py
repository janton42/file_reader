#!/usr/bin/env python3

# from csv_reader import get_active_users, get_audit_users, audit_status_changer


from csv_reader import FileHandler

def main():

	output = ''

	file_purpose = input("Is this for an external audit (yes/no)? ")

	if file_purpose == 'yes':
		file_name = 'moss_adams_sample'
		output = FileHandler.get_audit_users('./static/' + file_name + '.csv')
		FileHandler.audit(output)

	elif file_purpose == 'no':
		users_file_name = input('Enter the user list file name: ')
		contracts_file_name = input('Enter the contract list file name: ')
		active_users = FileHandler.get_active_users('./static/' + users_file_name + '.csv')
		active_contract = FileHandler.get_active_contracts()
		print('There are ', len(output), 'TIP users with systems access')

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


