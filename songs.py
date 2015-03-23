from bs4 import BeautifulSoup

import urllib2
response = urllib2.urlopen('http://www.linkersweddingsolutions.com/weddingsongs/list-of-wedding-songs-from-hindi-movies.html')
html = response.read()
links = []
rows = []

soup = BeautifulSoup(html)

table = soup.find('table', {'class': 'download'})

for row in table.findAll('tr'):
    matter = row.findAll('td')
    print 'matter is', matter.prettify()

"""
rows.append(matter[0].contents)
    links.append(matter[3])

key = str(row[::1])
    links[key] = row[::3]
soup = soup.select('a[href^="http://www.mymp3singer.com/get.php?"]')
for link in soup:
    links.append(str(link['href']))

response = urllib2.urlopen(links[0])
html = response.read()

print 'response is', response.info()
file_size_dl = 0


f = open('testFile.mp3', 'wb')
while True:
    buffer = response.read(8192)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
f.close()
"""
