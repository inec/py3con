#!/usr/bin/python3
import urllib.request, json, time
def GoogGeoAPI(address,api="",delay=5):
  base = r"https://maps.googleapis.com/maps/api/geocode/json?"
  addP = "address=" + address.replace(" ","+")
  GeoUrl = base + addP + "&key=" + api
  response = urllib.request.urlopen(GeoUrl)
  jsonRaw = response.read()
  print(jsonRaw)
  jsonData=jsonRaw
  #jsonData = xxjson.loads(jsonRaw)
  if jsonData['status'] == 'OK':
    resu = jsonData['results'][0]
    finList = [resu['formatted_address'],resu['geometry']['location']['lat'],resu['geometry']['location']['lng']]
  else:
    finList = [None,None,None]
  time.sleep(delay) #in seconds
  return finList
test = r"1600 Amphitheatre Parkway, Mountain View, CA"
test = r"R1A1S1"
geoR = GoogGeoAPI(address=test)
print(geoR)
