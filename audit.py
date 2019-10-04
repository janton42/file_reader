#!/usr/bin/env python3

# from csv_reader import get_active_users, get_audit_users, audit_status_changer
from url_opener import open_url, url_builder

from csv_reader import FileHandler

def main():

	file_name = ''
	output = ''

	file_purpose = input("Is this for an external audit (yes/no)? ")

	if file_purpose == 'yes':
		file_name = 'moss_adams_sample'
		output = FileHandler.get_audit_users('./static/' + file_name + '.csv')
	elif file_purpose == 'no':
		file_name = 'user_data'
		output = FileHandler.get_active_users('./static/' + file_name + '.csv')

	if file_purpose == 'yes':

		test_group = {}
		test_group_counter_raw = input("Enter group number to audit (1-5): ")
		test_group_counter = int(test_group_counter_raw)

		for contract in output:
			if test_group_counter == 1:
				test_group_counter += 1	
				while test_group_counter < 7:
					test_group[test_group_counter-1] = output[test_group_counter]['Contract ID']
					test_group_counter += 1
			elif test_group_counter == 2:
				test_group_counter = 10
				while test_group_counter <= 17:
					test_group[test_group_counter-1] = output[test_group_counter]['Contract ID']
					test_group_counter += 1
			elif test_group_counter == 3:
				test_group_counter = 18
				while test_group_counter <= 25:
					test_group[test_group_counter-1] = output[test_group_counter]['Contract ID']
					test_group_counter += 1
			elif test_group_counter == 4:
				test_group_counter = 26
				while test_group_counter <= 33:
					test_group[test_group_counter-1] = output[test_group_counter]['Contract ID']
					test_group_counter += 1
			elif test_group_counter == 5:
				test_group_counter = 26
				while test_group_counter <= 33:
					test_group[test_group_counter-1] = output[test_group_counter]['Contract ID']
					test_group_counter += 1

		for contract in test_group:
			contract_id = test_group[contract]

			url = url_builder(contract_id)
			open_url(url)

		print(test_group)

		next_group = input("Would you like to audit another group (yes/no)? ")
		if next_group == 'yes':
			main()
		else:
			print('Goodbye!','\n','*****************')





if __name__ == '__main__':
	main()


