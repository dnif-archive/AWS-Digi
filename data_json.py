import requests
import json
import re

#website from where we are fetching data
solditems = requests.get('http://www.webiron.com/abuse_feed//?format=json') 
data = solditems.json()

'''
some data is not in standard format.
to make data consistent and readable format.
writing data in data.json which is in readable format.
Make sure you have LogEvent and EvtLen element in your every json element.
'''

with open('data.json', 'a') as f:
    for i in data:
	i['LogEvent'] = 'Trial'
	i['EvtLen'] = 213
	i['event_emails'] = i['event_emails'][0]
	if i.get("days_unresolved"):
        	m = re.search('>(.*?)<', i["days_unresolved"])
        	i["days_unresolved"] = m.group(1) if m else i["days_unresolved"]
    json.dump(data, f , indent=6)
