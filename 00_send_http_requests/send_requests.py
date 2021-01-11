import httplib2
import urllib
import json

body = {
	'client_id':'SZCOBMRGNFYUY2N3IQCJ5Z0FSHMNL1MFZX5OKUQVDDT2WUBY',
	'client_secret':'GGXGUKIRW5ZS3WHY15MVLMKASIKV04BC3M5FEGQHUV5B4JV1'
}
	

url = "http://0.0.0.0:5000/createHello"

h = httplib2.Http()
header, content = h.request(url, 'POST', body=urllib.parse.urlencode(body))

print(content)