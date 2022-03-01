import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
data = urllib.request.urlopen(url, context=ctx).read()
data = data.decode()


tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
print('Count: ', len(counts) )
sum = 0
for item in counts:
    sum = sum + int(item.find('count').text)
print('Sum: ', sum)
