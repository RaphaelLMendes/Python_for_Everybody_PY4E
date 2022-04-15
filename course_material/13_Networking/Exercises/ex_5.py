'''
Exercise 5: (Advanced) 

Change the socket program so that it only shows data after the headers 
and a blank line have been received. Remember that recv receives 
characters (newlines and all), not lines.

'''

import socket, re

#url = input("Write a URL: ")
url = "http://data.pr4e.org/page1.htm"

array = url.split('/')

#creating my socket object
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecting to the url specified on port 80
try:
    mysocket.connect((array[2],80))

    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysocket.send(cmd)

    break_line_detected = False

    while True:
        data = mysocket.recv(512)
        if len(data) < 1 :
            break

        data_decoded = data.decode()

        if not break_line_detected:
            # finding all occurences of new lines
            all_nl = [i for i, x in enumerate(data_decoded) if x == '\n']

            break_line = 0

            for i in range(1,len(all_nl)):
                diff = all_nl[i] - all_nl[i-1]
                if diff < 3:
                    break_line = all_nl[i]
                    break_line_detected = True
                    print(data_decoded[break_line:])
                    break
        else:
            print(data_decoded)

    mysocket.close()
except:
    print("Improperly formatted or non-existent URL")