#The file downloads songs all audio songs from "http://www.linkersweddingsolutions.com/weddingsongs/list-of-wedding-songs-from-hindi-movies.html":
#Work in progress
from bs4 import BeautifulSoup

import urllib2

response = urllib2.urlopen('http://www.linkersweddingsolutions.com/weddingsongs/list-of-wedding-songs-from-hindi-movies.html')
html = response.read()
links = []

soup = BeautifulSoup(html)
soup = soup.select('a[href^="http://www.mymp3singer.com/get.php?"]')
for link in soup:
    links.append(str(link['href']))

# work here
response = urllib2.urlopen(links[0])
html = response.read()

print 'response is', response.info()
file_size_dl = 0
bufferSize = 8192
f = open('testFile.mp3', 'wb')
while True:
    buffer = response.read(bufferSize)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
f.close()
