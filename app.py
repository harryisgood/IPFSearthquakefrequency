from flask import Flask, request
import sys
import requests
import json
import geocoder
from countrygroups import EUROPEAN_UNION

app = Flask(__name__)
DATA='earthquake_data.txt'
# @app.route("/")
# def hello():
#     return "<h1 style='color:blue'>Hello There!</h1>"

def calculate_quake_likeliness(g):
    score = 100
    #output = subprocess.check_output(["ipfs", "cat", DATA, '>', DATA])
    # output = output.decode('utf-8')
    # output = output.split(' ')[1]
    g = geocoder.bing([46.765265,31.001662], method='reverse', key='AiBUtyu12bCAwVjxDKgaoKHUxrbb7szSUA2yRqB1RM01sS1HjD1Bu932reTaT9Pa')#)str(request.remote_addr))

    countries = []
    f=open(DATA, 'r')
    lines = f.readlines()
    for line in lines:
    	country = line.split(' ')[-1]
    	countries.append(country)

    if g.country not in EUROPEAN_UNION.names:
    	return 'Currently we don\'t have a score for your location yet...'
    elif g.country in EUROPEAN_UNION.names:
    	coords = g.latlng
    	if coords[0] <= 44.7 and coords[1] <= 31.2 and coords[1] >= 5 and coords[0] >= 35:
    		return 'There is a high probability of Earthquakes in this country'
    	else:
    		return 'This is a safe part of Europe...for now...'
    elif g.country in countries:
    	return 'There is a high probability of Earthquakes in this country'

@app.route('/')
def index():
    
    g = geocoder.bing('86.44.241.218', key='AiBUtyu12bCAwVjxDKgaoKHUxrbb7szSUA2yRqB1RM01sS1HjD1Bu932reTaT9Pa')#)str(request.remote_addr))
    #print((g.country))
    return calculate_quake_likeliness(g)
    #return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(port='5000')