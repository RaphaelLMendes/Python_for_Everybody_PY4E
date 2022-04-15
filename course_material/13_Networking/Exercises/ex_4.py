'''
Exercise 4: 

Change the urllinks.py program to extract and count paragraph (p) 
tags from the retrieved HTML document and display the count of the 
paragraphs as the output of your program. Do not display the paragraph 
text, only count them. Test your program on several small web pages 
as well as some larger web pages.

'''

import urllib.request, urllib.parse, urllib.error

#url = input("Write a URL: ")
url = "https://twitter.com/home"

# Example http://data.pr4e.org/page1.htm

#array = url.split('/')


fhand = urllib.request.urlopen(url)

counter_chars = 0

for line in fhand:
    counter_chars += len(line)

    if counter_chars > 3000:
        diff = counter_chars - 3000
        if diff > len(line):
            continue
        diff = diff*-1
        line_decode = line.decode().strip()
        print( line_decode[:diff] )
    else:
        print( line.decode().strip() )

print(counter_chars)
