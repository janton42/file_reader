#!/usr/bin/env python3

class FilterLists(object):
	"""docstring for FilterLists"""

	l3_countries = ['Australia','Austria','Canada','Denmark','Finland','France','Germany','Ireland','Italy','Liechtenstein','Luxembourg','Monaco','Netherlands','Norway','Portugal','Spain','Sweden','Switzerland','United Kingdom','United States','American Samoa','Guam', 'Puerto Rico','U.S. Virgin Islands','Northern Mariana Islands']

	l3_whitelist = ['23043173']
		
	def __init__(self, arg):
		super(FilterLists, self).__init__()
		self.arg = arg
		