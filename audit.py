#!/usr/bin/env python3

from csv_reader import get_active_users, get_audit_users, audit_status_changer
from url_opener import open_url, url_builder

def main():

	output_1 = get_audit_users('./static/moss_adams_sample.csv')
	output_2 = get_active_users('./static/user_data.csv')

	print(len(output_1))



	test_group = {}
	test_group_counter_raw = input("Enter group number to audit (1-5): ")
	test_group_counter = int(test_group_counter_raw)

	for contract in output_1:
		if test_group_counter == 1:
			test_group_counter += 1	
			while test_group_counter < 10:
				test_group[test_group_counter-1] = output_1[test_group_counter]['Contract ID']
				test_group_counter += 1
		elif test_group_counter == 2:
			test_group_counter = 10
			while test_group_counter <= 17:
				test_group[test_group_counter-1] = output_1[test_group_counter]['Contract ID']
				test_group_counter += 1
		elif test_group_counter == 3:
			test_group_counter = 18
			while test_group_counter <= 25:
				test_group[test_group_counter-1] = output_1[test_group_counter]['Contract ID']
				test_group_counter += 1
		elif test_group_counter == 4:
			test_group_counter = 26
			while test_group_counter <= 33:
				test_group[test_group_counter-1] = output_1[test_group_counter]['Contract ID']
				test_group_counter += 1
		elif test_group_counter == 5:
			test_group_counter = 26
			while test_group_counter <= 33:
				test_group[test_group_counter-1] = output_1[test_group_counter]['Contract ID']
				test_group_counter += 1





	print(test_group)

	# for contract in output_1:
	# 	test_group_counter = 1
	# 	while test_group_counter <= 6:	
	# 		test_group_1[test_group_counter] = output_1[test_group_counter]
	# 		test_group_counter += 1

	# test_group_2 = {}
	# for contract in output_1:
	# 	test_group_counter = 6
	# 	while test_group_counter <= 10:	
	# 		test_group_2[test_group_counter] = output_1[test_group_counter]
	# 		test_group_counter += 1

	# # print(len(output_1))


	# print(contract_id_test)

	for contract in test_group:
		contract_id = test_group[contract]

		url = url_builder(contract_id)
		open_url(url)

	# i = 0
	# while i < len(output):
	# 	print(output[i])
	# 	i += 1

	# print(len(output[110]))
	
	# print(output[110])

	# print(output[0])
	# single_user = output[222]
	# full_name = single_user['full_name']
	# uid = single_user['worker_user_id']

	# print(full_name, uid)

if __name__ == '__main__':
	main()


