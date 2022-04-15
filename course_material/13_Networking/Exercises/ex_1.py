'''
Exercise 1: 

Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
You can use split('/') to break the URL into its component parts so you can extract the 
host name for the socket connect call. Add error checking using try and except to handle 
the condition where the user enters an improperly formatted or non-existent URL.

'''

import socket

url = input("Write a URL: ")
#url = "http://data.pr4e.org/page1.htm"

array = url.split('/')

#creating my socket object
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecting to the url specified on port 80
try:
    mysocket.connect((array[2],80))

    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if len(data) < 1 :
            break
        print(data.decode())

    mysocket.close()
except:
    print("Improperly formatted or non-existent URL")