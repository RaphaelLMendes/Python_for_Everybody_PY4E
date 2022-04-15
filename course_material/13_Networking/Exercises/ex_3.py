'''
Exercise 3: 

Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
(2) displaying up to 3000 characters, and (3) counting the overall number of characters 
in the document. Dont worry about the headers for this exercise, simply show the first 
3000 characters of the document contents.

'''

import urllib.request, urllib.parse, urllib.error

#url = input("Write a URL: ")
url = "http://data.pr4e.org/page1.htm"

# Example http://data.pr4e.org/page1.htm

#array = url.split('/')


fhand = urllib.request.urlopen(url)

counter_chars = 0

for line in fhand:
    counter_chars += len(line)

    if counter_chars > 3000:
        diff = counter_chars - 3000
        print( line.decode().strip()[:-diff] )
    else:
        print( line.decode().strip() )

print(counter_chars)
