import requests, json

headers = {'apikey': '21d9789c1a811465a15f752aae0d524f'}

def get_nearest_data(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon)
    response = requests.get(
        url,
        headers=headers)
    data = response.json()
    return data

# def get_detailed_data_by_id(id):
#     url = "https://airapi.airly.eu/v1/sensor/measurements?sensorId="+str(id)
#     response = requests.get(
#         url,
#         headers=headers)
#     data = response.json()
#     return data
