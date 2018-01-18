import requests, json

headers = {'apikey': '1f1a2d1db77740efb5897fc911de0b52'}

def get_geolocation(ip):
    send_url = 'http://freegeoip.net/json/' + ip
    r = requests.get(send_url)
    j = json.loads(r.text)
    geolocation = {}
    geolocation['lat'] = str(j['latitude'])
    geolocation['lon'] = str(j['longitude'])
    return geolocation

def get_nearest_data(lat, lon):
    url = "https://airapi.airly.eu/v1/nearestSensor/measurements?latitude=" + str(lat) + "&longitude=" + str(lon) + "&maxDistance=1000000"
    response = requests.get(
        url,
        headers=headers)
    data = response.json()
    return data

def get_detailed_data_by_id(id):
    url = "https://airapi.airly.eu/v1/sensor/measurements?sensorId="+str(id)
    response = requests.get(
        url,
        headers=headers)
    data = response.json()
    return data
