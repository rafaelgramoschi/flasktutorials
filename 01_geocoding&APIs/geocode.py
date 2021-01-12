import httplib2 # comprehensive http lib
import json # convert in memory object to a serialized JSON representation

def getGeocodeLocation(inputString):
	
	locationString = inputString.replace(" ", "+")
	
	url = ( 'https://nominatim.openstreetmap.org/search?q={}&format=json&limit=1'.format(locationString) )

	h = httplib2.Http()
	
	header, content = h.request(url, 'GET')
	result = json.loads(content)

	# debug/understand response
	#print( "Response header: {}".format(header) )
	#print()
	#print( "Result: {}\n".format(result) )
	
	if not result:
		lat, lon = None, None
	else:
		lat = result[0].setdefault('lat',None)
		lon = result[0].setdefault('lon',None)

	return (lat, lon)

if __name__ == "__main__":
	roma = getGeocodeLocation("Roma Italia")
	wrong = getGeocodeLocation("Sydney Austrailia") # wrong on purpose
	print(roma, wrong)