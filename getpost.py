import urllib
import json
import requests

url = 'http://www.webiron.com/abuse_feed//?format=json'
url1 = 'http://192.168.1.102:9234/json/receive'

response = urllib.urlopen(url)
data_json = json.loads(response.read())


#for i in data_json:
#	i['LogEvent'] = 'Trial'
#	i['EvtLen'] = 213

print json.dumps(data_json,indent=6)

send_data = json.dumps(data_json)

headers = {'Content-type': 'application/json'}

requests.post(url1,data=send_data)

r = requests.post(url1,data=send_data,headers=headers)

print r.json
