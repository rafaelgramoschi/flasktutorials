OSI Layers

Application
Presentation
Session
Transport
Network
Data Link
Physical

on top of the OSI you could say there are:

Messaging (XML,JSON)
web services (SOAP, REST)


RESTful API (Representational state transfer)

Constraints:
1. client-server
2. stateless
3. cachable
4. Layered System (i talk to a server which talks to others i don't know about)
5. Code on Demand (the server might send client-side executable code on demand)
6. uniform interface (different machines talk to each other)

HTTP is a "pull" protocol


HTTP request (header,blank line, body)


header			| (the first line) the request line [HTTP verb, URI, HTTP version number] e.g.: GET /index.html HTTP/1.1
				| optional request headers (describe params of requests) [name:value, pairs] e.g: 
blank line		| separates the header from the body
body (optional) | additional information we want to send to the server

e.g.:
GET index.html HTTP/1.1
Host: www.site.com
Accept: image/gif, image/jpeg, */*
Accept-Language: en-us
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0
Content-Length: 35

Id=1234&name=Home+Table



HTTP response (header, blank line, body)

header:		(first line) status line [HTTP version, status code, reason phrase("200 OK, 404 Not Found, 403 Forbidden") ] e.g.: 
			optional response headers [name:value, pairs]
blank line: separates the header from the body
body:		contains the requested resource

e.g.:
HTTP/1.1 200 OK
Date: Tue, 05 Jan 2021 13:46:00 GMT
Server: Apache/1.3.29 (Win32)
Last-Modified: Sat, 07 Feb 2014
ETag: "0-23-4024c3a5":
ContentType: text/html
ContentLength: 35
Connection: KeepAlive
KeepAlive: timeout=15, max=100

<h1>Welcome to my home page!</h1>


USING POSTMAN OR CURL TO SEND HTTP REQUESTS

There are some exceptions, but for most use cases:

HTTP <--> CRUD
GET <--> READ
POST<--> CREATE
PUT <--> UPDATE/CREATE
PATCH <--> UPDATE
DELETE-<-->DELETE

		 [GET] curl http:/0.0.0.0:5000/readHello -v
		
		[POST] curl http://0.0.0.0:5000/createHello -d '{"value":"name"}' -v
		  [OR] curl http://0.0.0.0:5000/createHello -F "value=name&other=other" -v

[PUT (UPDATE)] curl http://0.0.0.0:5000/updateHello -X PUT -d '{"value":"name"}' -v
		  [OR] curl http://0.0.0.0:5000/updateHello -X PUT -F "value=name&other=other" -v
	  
	  [DELETE] curl http://0.0.0.0:5000/deleteHello -X DELETE -v

-v verbose
-H custom header(s) to send
-d HTTP POST data (body)
-F form data (multipart MIME data)
-X request command to use (HTTP verb)

