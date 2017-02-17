#   Author:       Parker Misch
#   Title:        Lions Data Scrape
#   Description:  Parsing state code and zipcode from all Lions Clubs in the US
#   Date:         2/17/17

#from bs4 import BeautifulSoup as bsoup
import requests as rq
import re

#states minus CA, IN, PA, and TX
states = [ "AK", "AL", "AR", "AZ", "CO", "CT", "DC", "DE", "FL",
           "GA", "HI", "IA", "ID", "IL", "KS", "KY", "LA", "MA",
           "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND",
           "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR",
           "RI", "SC", "SD", "TN", "UT", "VA", "VT", "WA", "WI",
           "WV", "WY"]


data = []
for state in states:
  #advanced search url
	url = 'https://directory.lionsclubs.org/SearchHandler.ashx?contactname=&clubname=&orgtype=1&orglanguage=0&country=US&state=' + state + '&city=&zip=&type=extended'
	r = rq.get(url)

  #parse the content of the get request
  #state code followed by a 5 digit number is the desired data
	new_data = re.findall(state + ' \d{5}', r.content)
  data += new_data

  #printing the state and how many zipcodes found in the state
  print(state)
	print(len(new_data))

#states that the website did not support an advanced search on
messed_up_states = ["california", "indiana", "pennsylvania", "texas"]
messed_up_states_codes = ["CA", "IN", "PA", "TX"]

for i, state in enumerate(messed_up_states):
  #general search url
	url = 'https://directory.lionsclubs.org/SearchHandler.ashx?data=' + state + '&type=normal'
	r = rq.get(url)

  #state code followed by a 5 digit number is the desired data
	new_data = re.findall(messed_up_states_codes[i] + ' \d{5}', r.content)
  data += new_data

  #printing the state and how many zipcodes found in the state
  print(messed_up_states_codes[i])
  print(len(new_data))

#print length of final list
print(len(data))

#output the data to a textfile to be mapped
filename = open('html_data.txt','w')
filename.write('\n'.join(data))
