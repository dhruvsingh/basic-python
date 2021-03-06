from bs4 import BeautifulSoup

import urllib2
from datetime import datetime

now = datetime.now()

links = {}

response = urllib2.urlopen('http://www.linkersweddingsolutions.com/weddingsongs/list-of-wedding-songs-from-hindi-movies.html')
html = response.read()
soup = BeautifulSoup(html)

table = soup.find('table', {'class': 'download'})

for row in table.findAll('tr'):
    matter = row.findAll('td')
    link = matter[2].find('a')
    key = str(matter[0].text.strip())
    links[key] = str(link['href'].strip())

# Code to download the songs in links above
file_size_dl = 0

for key, value in links.iteritems():
    response = urllib2.urlopen(value)
    file_name = 'YOURSAVELOCATION/{0}/.mp3'.format(key)
    f = open(file_name, 'wb')
    while True:
        buffer = response.read(8192)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
    f.close()

print 'the time taken is', datetime.now() - now
