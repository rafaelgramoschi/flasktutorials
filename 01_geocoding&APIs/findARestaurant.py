from geocode import getGeocodeLocation
import httplib2
import json
import urllib

# render properly even if ascii chars are found (or non english chars)
# this nullifies the print() function: it won't print no more
#import sys
#import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

client_id = "FOURSQUARE_CLIENT_ID"
client_secret = "FOURSQUARE_CLIENT_SECRET"

def getJsonFrom(url):
	http = httplib2.Http()
	header, content = http.request(url, 'GET')
	result = json.loads(content)
	return result

def getVenueImage(venueId):
	url = "https://api.foursquare.com/v2/venues/{}/photos?client_id={}&client_secret={}&v=20200110".format(venueId, client_id, client_secret)
	result = getJsonFrom(url)
	
	if result['meta']['code'] == 429 and result['meta']['errorType'] == "quota_exceeded":

		result = "quota_exceeded"
	
	else:
	
		imgs = result['response']['photos'].setdefault('items',None)
		"""print("imgs")
		print(result['response'])
		print()
		"""
		if not imgs:
			result = None
		else:
			prefix = imgs[0]['prefix']
			suffix = imgs[0]['suffix']
			result = "{}300x300{}".format(prefix,suffix)

	return result

def findARestaurant(mealType, location):
	
	print()

	lat, lon = getGeocodeLocation(location)
	
	if lat and lon:
		url = "https://api.foursquare.com/v2/venues/search?"\
			+ "radius=50000&limit=1&v=20200110"\
			+ "&ll={},{}&query={}".format(lat,lon,mealType)\
			+ "&client_id={}&client_secret={}".format(client_id,client_secret)
		
		result = getJsonFrom(url)
		# debug:
		#print("\n{}\n".format(result) )

		if not result['response']['venues']:
			result = {}
		else:
			name = result['response']['venues'][0]['name']

			venueId = result['response']['venues'][0]['id']

			location = result['response']['venues'][0]['location']
			address = location.setdefault('address',None)
			place_lat, place_lon = location['lat'], location['lng']
			country = location['cc']

			result = {"name": name, "address":address, "image": getVenueImage(venueId)}
			#print( "name: {}\naddress: {},{}\nlat:{:.2f}, lon:{:.2f}".format(name, address, country, place_lat, place_lon) )
	else:
		print("No place in the world found with the name '{}'.\n".format(location))
		result = None

	print(result)

if __name__ == "__main__":

	print("\n[*] Running...")
	print("[*] Using https://api.foursquare.com/v2/venues/search")

	findARestaurant("pizza","tokyo, japan")
	findARestaurant("tacos","jakarta, indonesia")
	findARestaurant("tapas","maputo, mozambique")
	findARestaurant("Falafel","cairo, egypt")
	findARestaurant("spaghetti","new delhi, india")
	findARestaurant("capuccino","geneva, switzerland")
	findARestaurant("sushi","los angeles, california")
	findARestaurant("steak","la paz, bolivia")
	findARestaurant("gyros","sydney austrailia")
