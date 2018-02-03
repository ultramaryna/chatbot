import requests, json

headers = {'apikey': '1f1a2d1db77740efb5897fc911de0b52'}

def get_geolocation(ip):
    send_url = 'http://ip-api.com/json/' + ip
    response = requests.get(send_url)
    data = response.json()
    geolocation = {}
    geolocation['lat'] = str(data['lat'])
    geolocation['lon'] = str(data['lon'])
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
