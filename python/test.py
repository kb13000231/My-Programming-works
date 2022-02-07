import re
a = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
b = re.findall('href="(.+)"',a)
print(b)
