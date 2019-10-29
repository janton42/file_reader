#!/usr/bin/env python3

class FilterLists(object):
	"""docstring for FilterLists"""

	l3_countries = ['Australia','Austria','Canada','Denmark','Finland','France','Germany','Ireland','Italy','Liechtenstein','Luxembourg','Monaco','Netherlands','Norway','Portugal','Spain','Sweden','Switzerland','United Kingdom','United States','American Samoa','Guam', 'Puerto Rico','U.S. Virgin Islands','Northern Mariana Islands']

	l3_whitelist = ['22478593','22841161','22581299','23043173','21873943','21911185','21919225','22066588','22347317','22457432','22704694','22663732','22814728','22964156','22961290','22938226','22979023','23019534','23037843','23045996']
		
	def __init__(self, arg):
		super(FilterLists, self).__init__()
		self.arg = arg
		