#!/usr/bin/env python3

from bs4 import BeautifulSoup
import lxml
import requests
import re
import csv

def scrape_gdacs():
  url = 'http://www.gdacs.org/XML/RSS.xml'
  resp = requests.get(url)
  soup = BeautifulSoup(resp.content, features="xml")
  items = soup.findAll('item')

  return items

def create_events_dict(items):

  all_events = {}
  counter_1 = 0
  
  for i in items:
    event_type = i.find('eventtype').text
    severity = i.find('alertlevel').text
    if event_type != 'DR':
      event = {}
      resources = i.find('resources')
      resource_list = resources.findAll('resource')
      for a in resource_list:
        if a['id'] == 'impact_xml':
          event['type'] = event_type
          event['severity'] = severity
          event['detail'] = a['url']
          counter_1 += 1
          all_events[counter_1] = event

  disaster_details = {}
  counter_2 = 0

  for e in all_events:
    response = requests.get(all_events[e]['detail'])
    soup_2 = BeautifulSoup(response.content, features="xml")
    datums = soup_2.findAll('datums')
    for a in datums:
      if a['alias'] == 'City':
        datum = a.findAll('datum')
        for d in datum:
          disaster = []
          scalars = d.findAll('scalar')
          for s in scalars:
            if s.find('name').text == 'NAME':
              disaster.append(s.value.text)
            elif s.find('name').text == 'COUNTRY':
              disaster.append(s.value.text)
              disaster.append(all_events[e]['type'])
              disaster.append(all_events[e]['severity'])

          if len(disaster) > 0:
            counter_2 += 1
            disaster_details[counter_2] = disaster

  return disaster_details
