import requests
import json
import datetime as dt
from datetime import timedelta
import geocoder

def earthquake(f):
    today = dt.date.today()
    lastmonth = today - timedelta(days=3000)
    
    params = {"format": "geojson", "starttime": lastmonth, "endtime": str(today), "alertlevel": "orange"}
    data = requests.get(f, params = params)
    data = json.loads(data.text)
    return data

f = r"https://earthquake.usgs.gov/fdsnws/event/1/query?"
a = earthquake(f)

f=open('earthquake_data.txt', 'w')
for i in (a["features"]):
    info = str(i["properties"]["time"]) + ' ' + str(i["properties"]["place"])+ ' ' + str(i["properties"]["cdi"])
    f.write(info)
    f.write('\n')
f.close()
