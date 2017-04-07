import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = raw_input('Enter your URL - ')
url_split = url.split('/')
host = url_split[2]

try:
	mysock.connect(( host, 80))
	mysock.send('GET https://support.office.com/en-us/article/Create-and-use-your-own-template-a1b72758-61a0-4215-80eb-165c6c4bed04#bmpp HTTP/1.0\n\n')

	while True:
	    data = mysock.recv(4096)
	    if ( len(data) < 1 ) :
	        break
	    print data;

	mysock.close()
except SyntaxError:
	print "you should insert a URL with protocol/host/page"