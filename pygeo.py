"""
Hey dom, didn't bother with the library im just going to http in as google is a web api
Make sure your python runtime or venv is 3.8
These package managers make keeping your software up to date a lot easier
Windows: https://chocolatey.org/
Mac: https://brew.sh/

windows: install - choco install python3 --pre
         uchoco upgrade python3 --pre
mac: install - brew install python3
"""
#this guy is important, this is an http library so go ahead and install it with
# pip install requests - inside your project root on terminal
import requests

#lets just store all of the api urls as constants - or whatever python does with immutables or lack there of,
#these should be constant values in any language that supports it with private protection (unless it is an enum)
directions_api = 'https://maps.googleapis.com/maps/api/directions/json'
geocode_api = 'https://maps.googleapis.com/maps/api/geocode/json'
geolocate_api = 'https://www.googleapis.com/geolocation/v1/geolocate'
# There are more, these for now

# PUT YOUR OWN API KEY IN HERE
API_KEY="PUTINYOUROWNAPIKEYHERE"
#to find out what params to bind i recommend reading the google documentation
# here: https://developers.google.com/maps/documentation/

#just store all the params in here
address= dict(
    address="202+queen+street+west,Toronto,Ontario",
    key=API_KEY
)

# more params
directions = dict(
    origin='Toronto,ON',
    destination='Vancouver,BC',
    waypoints='Calgary,AB|Red+Deer,AB',
    sensor='false',
    key=API_KEY
)

geolocate = dict(
key=API_KEY
)

# easily bind your variables to the named function parameters and make the get request to the url
resp = requests.get(url=directions_api, params=directions)
#you are going to get back a response object, so store it in memory so you can view - we use .json() to parse the json output
# not all websites give you back json, but google apis gives data in this format and xml. JSON are just KV pairs of name value.
data = resp.json()
print(data)
print("##########################################################################################################################################################")

# this one is a little different - it has to send a post request
# see here for http methods - https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
#wash rinse repeat for any of the apis you would like to use - you can develop these web API's in php, python, java(my favorite + Spring Boot), Node.js and GO
# if you are interested make sure you study how to secure it with  https://oauth.net/ or API key like we are doing now
resp = requests.get(url=geocode_api, params=address)
data = resp.json()
print(data)
print("##########################################################################################################################################################")

#and finally where we are now
resp = requests.post(url=geolocate_api, params=geolocate)
data = resp.json()
print(data)
# at the end of the day try not to think so much about the libraries until you know what the machine is doing
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview - simple http protcol makes implementation very easy