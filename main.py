#!/usr/bin/env python3


from audits import Auditor

# from emailer import Emailer



def main():

	Auditor.active_users_without_contracts()
	Auditor.end_dates()
	

if __name__ == '__main__':
	main()


