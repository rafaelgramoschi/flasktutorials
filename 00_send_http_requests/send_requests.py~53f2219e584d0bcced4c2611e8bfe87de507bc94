import httplib2
import urllib
import json

body = {
	"val":123
}
	

url = "http://0.0.0.0:5000/createHello"

h = httplib2.Http()
header, content = h.request(url, 'POST', body=urllib.parse.urlencode(body))

print(content)
