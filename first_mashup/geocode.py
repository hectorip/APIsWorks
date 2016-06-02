import httplib2
import json

def getGeocodeLocation(inputString):

    googke_api_key = "KEY"
    locationString = inputString.replace(" ", "+")

    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    http = httplib2.Http()
    res = json.loads(http.request(url, 'GET')[1]) # Getting First result

    latitude = res['results'][0]['location']['lat']
    longitude = res['results'][0]['location']['lng']

    return latitude, longitude
