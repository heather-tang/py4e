import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL ')
cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
lst = list()
tags = soup('a')
for tag in tags:
    lst.append(tag.get('href', None))
# for i in lst:
#     print(i)
print("Retrieving: ", url)
print("Retrieving: ", lst[pos-1])

i = 0
while i < cnt-1:
    url = lst[pos-1]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    lst = list()
    for tag in tags:
        lst.append(tag.get('href', None))
    print("Retrieving: ", lst[pos-1])
    i = i + 1
    
##### another exercise ####  
    
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
# It's important to decode the tags
sum = 0
tags = soup('span')
for tag in tags:
    num = re.findall('[0-9]+', tag.decode())
    for i in num:
        sum = sum + float(i)
#
print(int(sum))
