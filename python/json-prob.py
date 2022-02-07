import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    data_loc = input('Enter location: ')
    if len(data_loc) < 1:
        break
    uh = urllib.request.urlopen(data_loc, context=ctx )
    data = uh.read()
    info = json.loads(data)
    total = 0
    for i in info['comments']:
        total += i['count']
    print(total)
