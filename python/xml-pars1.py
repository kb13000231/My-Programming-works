import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url_data = urllib.request.urlopen(address, context=ctx).read()
    tree = ET.fromstring(url_data)
    ls = tree.findall('comments/comment')
    total = 0
    for item in ls:
        total += int(item.find('count').text)
    print(total)
