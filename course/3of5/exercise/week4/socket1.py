import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = raw_input('Enter your URL - ')
url_split = url.split('/')
host = url_split[2]

try:
	mysock.connect(( host, 80))
	mysock.send('GET'+url+' \n\n')

	while True:
	    data = mysock.recv(4096)
	    if ( len(data) < 1 ) :
	        break
	    print data;

	mysock.close()
except SyntaxError:
	print "you should insert a URL with protocol/host/page"
