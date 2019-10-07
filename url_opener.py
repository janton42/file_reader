#!/usr/bin/env python3

import webbrowser


def url_builder(contract_id):

	url = 'https://www.upwork.com/ab/c/2315977/contracts/' + contract_id + '#terms'

	return url

def open_url(url):

	a_website = url
	webbrowser.open(a_website, 2) # Equivalent to: webbrowser.open_new_tab(a_website)