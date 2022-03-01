import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
data = urllib.request.urlopen(url, context=ctx).read()
data = data.decode()


tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
print('Count: ', len(counts) )
sum = 0
for item in counts:
    sum = sum + int(item.find('count').text)
print('Sum: ', sum)

####

import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter the URL: ")
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)


sum = 0
for item in info['comments']:
    sum = sum + int(item["count"])

print('Sum = ', sum)


####

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(js)

print(json.dumps(js, indent=4))
place_id = js['results'][0]['place_id']
print('Place ID', place_id)
