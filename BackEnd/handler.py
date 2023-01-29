from flask import Flask
import json
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

APIKEY = "5ae2e3f221c38a28845f05b67974c00e6ed6d16556c0b2bd2763f6f0" 

def get_coordinants(point_of_interest):
    response = requests.get(f"https://api.opentripmap.com/0.1/en/places/geoname?name={point_of_interest}&apikey={APIKEY}")
    data = json.loads(response.text)
    lat = data["lat"]
    lon = data["lon"]
    return lat, lon



def get_attraction_list(point_of_interest, pg):

    lat, lon = get_coordinants(point_of_interest)

    response = requests.get(f"https://api.opentripmap.com/0.1/en/places/radius?radius=10000&lon={lon}&lat={lat}&apikey={APIKEY}")
    data = json.loads(response.text)
    xids = [ dest["properties"]["xid"] for dest in data["features"] 
        
        if (dest["properties"]["name"] != "" and ("historic" in dest["properties"]["kinds"] or "interesting_places" in dest["properties"]["kinds"]))
        
    ]

    sorted_xids = sorted(xids)

    res = {}
    count = 0
    i = 0
    while (i < len(sorted_xids) and count < 20):
        print(count)
        dest = sorted_xids[i]
        response = requests.get(f"http://api.opentripmap.com/0.1/en/places/xid/{dest}?apikey={APIKEY}")
        data = json.loads(response.text)
        res[dest] = {}
        try:
            res[dest]["name"] = data["name"]
        except:
            del res[dest]
            continue
        try:
            res[dest]["rate"] = data["rate"]
        except:
            pass
        try:
            res[dest]["addr"] = f"{data['address']['road']}, {data['address']['city']}, {data['address']['country']}"
        except:
            pass
        try:
            res[dest]["img"] = data["image"]
        except:
            pass
        try:
            res[dest]["discription"] = data["wikipedia_extracts"]["text"]
        except:
            pass
        count += 1
        i += 1
    

    return res







## unload this into json
@app.get('/attractions/<point_of_interest>/<pg>')
def attraction_list(point_of_interest, pg):

    dests = get_attraction_list(point_of_interest, int(pg))
    return {"attractions":dests}


