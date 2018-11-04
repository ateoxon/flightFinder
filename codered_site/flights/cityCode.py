import requests
import json
import pandas as pd

def getCodeDB(locations):
    print(locations)
    air = pd.read_csv('./flights/airports.csv')
    a = air.loc[air['iso_region']==locations]
    print("a")
    a = air.loc[air['iata_code'].notnull()]
    print(a['iata_code'].iloc[0])
    return a['iata_code'].iloc[1]

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

def getStateCode(state):
    state = state.lower()
    states = {
        "alabama" : "AL",
        "alaska" : "AK",
        "arizona" : "AZ",
        "arkansas" : "AR",
        "california" : "CA",
        "colorado" : "CO",
        "connecticut" : "CT",
        "delaware" : "DE",
        "florida" : "FL",
        "georgia" : "GA",
        "hawaii" : "HI",
        "idaho" : "ID",
        "illinois" : "IL",
        "indiana" : "IN",
        "iowa" : "IA",
        "kansas" : "KS",
        "kentucky" : "KY",
        "louisiana" : "LA",
        "maine" : "ME",
        "maryland" : "MD",
        "massachusetts" : "MA",
        "michigan" : "MI",
        "minnesota" : "MN",
        "mississippi" : "MS",
        "missouri" : "MO",
        "montana" : "MT",
        "nebraska" : "NE",
        "nevada" : "NV",
        "new-hampshire": "NH",
        "new-jersey" : "NJ",
        "new-mexico" : "NM",
        "new-york" : "NY",
        "north-carolina" : "NC",
        "north-dakota" : "ND",
        "ohio" : "OH",
        "oklahoma" : "OK",
        "oregon" : "OR",
        "pennsylvania" : "PA",
        "rhode-island" : "RI",
        "south-carolina" : "SC",
        "south-dakota" : "SD",
        "tennessee" : "TN",
        "texas" : "TX",
        "utah" : "UT",
        "vermont" : "VT",
        "virginia" : "VA",
        "washington" : "WA",
        "west-virginia" : "WV",
        "wisconsin" : "WI",
        "wyoming" : "WY",
        "american-samoa" : "AS",
        "district-of-columbia" : "DC",
        "federated-states-of-micronesia" : "FM",
        "guam" : "GU",
        "marshall-islands" : "MH",
        "northern-mariana-islands" : "MP",
        "palau" : "PW",
        "puerto-rico" : "PR",
        "virgin-islands" : "VI"
    }
    return states.get(state,0)
