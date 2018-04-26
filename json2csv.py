#libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd 


#connecting to website and request for the data
url = "http://www.webiron.com/abuse_feed/"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,"lxml")

#Selecting table 2 and taking row 2 since 1st row is for header
table = soup.find_all('table')[1]
rows = table.find_all('tr')[2:]


#replicating same data 
data = {
    '$LogEntryType' : [],
    '$LogTime' : [],
    '$AttackIP' : [],
    '$EntryEmail' : [],
    '$LogMessage' : [],
    '$Deliverables' : [],
    '$DaysUnresolved' : [],
    '$IncidentReported' : []	
}

#looping data to fetch data 
for row in rows:
    cols = row.find_all('td')
    data['$LogEntryType'].append( cols[0].get_text() )
    data['$LogTime'].append( cols[1].get_text() )
    data['$AttackIP'].append( cols[2].get_text() )
    data['$EntryEmail'].append( cols[3].get_text() )
    data['$LogMessage'].append( cols[4].get_text() )
    data['$Deliverables'].append( cols[5].get_text() )
    data['$DaysUnresolved'].append( cols[6].get_text() )
    data['$IncidentReported'].append( cols[7].get_text() )

#saving data in csv format
ThreatData = pd.DataFrame( data )
ThreatData.to_csv("abusefeed.csv")
