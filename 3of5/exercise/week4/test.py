import socket 
#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#now connect to the web server on port 44
s.connect(("en.wikipedia.org", 443))
s.send('GET https://en.wikipedia.org/wiki/Main_Page HTTP/1.0\n\n')
#it is necessary to read the infomation from the socket human readible 
while True:
    data = s.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

s.close()


