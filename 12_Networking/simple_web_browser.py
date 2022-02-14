import socket

# url 
url = 'data.pr4e.org'
path = 'page1.htm'

# #creating my socket object
# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Conecting to the url specified on port 80
# mysocket.connect((url,80))

# cmd = f'GET http://data.pr4e.org/{path} HTTP/1.0\r\n\r\n'.encode()
# mysocket.send(cmd)

# while True:
#     data = mysocket.recv(512)
#     if len(data) < 1 :
#         break
#     print(data.decode())

# mysocket.close()


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen(f'http://data.pr4e.org/{path}')

for line in fhand:
    print( line.decode().strip() )