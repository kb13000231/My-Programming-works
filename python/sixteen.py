import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ls = list()
url = input('Enter - ')
count = 0
while True:
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    a = url.split('_')
    b = a[2].split('.')
    ls.append(b[0])
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    c = tags[17]
    url = c.get('href', None)
    count += 1
    if count == 8:
        break
    else:
        continue
for i in ls:
    print(i)
