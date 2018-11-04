import requests
import json

# locations is of form city-state-country or city-country
def getCode(locations):
    resp = requests.get('https://api.skypicker.com/locations?type=slug&term={0}'.format(locations))
    if resp.text == '404: Not Found':
        return None

    return resp.json()['locations'][0]['code']

# accepts city codes retrieved with getCode(locations) for depart and arrive
def getFlights(depart, arrive):
    resp = requests.get('https://api.skypicker.com/flights?fly_from={0}&fly_to={1}&currency=USD'.format(depart, arrive))
    if resp.text == '404: Not Found':
        return None
    top5 = resp.json()['data'][0:4]

    return resp.json()['best_results'], top5
