import urllib
import json
import requests
import re

#website from where we are fetching data
url = 'http://www.webiron.com/abuse_feed//?format=json'

#localhost url with httplistener service running in ssh
# port 9234 is port for httplistener 
# port 9236 is port for httpslistener
url1 = 'http://192.168.1.101:9234/json/receive'

response = urllib.urlopen(url)
data_json = json.loads(response.read())

'''
some data is not in standard format.
to make data consistent and readable format
Make sure you have LogEvent and EvtLen element in your every json element.
'''

for i in data_json:
	i['LogEvent'] = 'Trial'
	i['EvtLen'] = 213
	i['event_emails'] = i['event_emails'][0]
	if i.get("days_unresolved"):
        	m = re.search('>(.*?)<', i["days_unresolved"])
        	i["days_unresolved"] = m.group(1) if m else i["days_unresolved"]

#print json.dumps(data_json,indent=6)

send_data = json.dumps(data_json)

headers = {'Content-type': 'application/json'}

requests.post(url1,data=send_data)

r = requests.post(url1,data=send_data,headers=headers)

print r.json
