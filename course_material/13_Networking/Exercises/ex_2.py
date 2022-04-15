'''
Exercise 2: 

Change your socket program so that it counts the number of characters it has 
received and stops displaying any text after it has shown 3000 characters. 
The program should retrieve the entire document and count the total number of 
characters and display the count of the number of characters at the end of 
the document.

'''

import socket

#url = input("Write a URL: ")
url = "http://data.pr4e.org/page1.htm"

# Example http://data.pr4e.org/page1.htm

array = url.split('/')

#creating my socket object
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecting to the url specified on port 80
try:
    mysocket.connect((array[2],80))

    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysocket.send(cmd)

    counter_chars = 0

    while True:
        data = mysocket.recv(512)
        if len(data) < 1 or counter_chars>3000:
            break
        if counter_chars>2488:
            remaining = 3000-counter_chars
            print(data.decode()[:remaining])
        else:
            print(data.decode())
        counter_chars += len(data.decode())

    mysocket.close()
    print(counter_chars)
except:
    print("Improperly formatted or non-existent URL")