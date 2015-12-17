from pprint import pprint as pp
import requests
#r = requests.get('http://www.crummy.com/software/BeautifulSoup/bs4/doc/')

#pp(r.status_code)
#pp(r.encoding)
#r.encoding = 'UTF-8'
#pp(r.encoding)
#pp(r.text)
#pp(r.content)

import urllib2
sock = urllib2.urlopen('https://vk.com/im?sel=157292280')
sock.getcode()
data = sock.read()
sock.close()
print(data)


'''
ri = requests.get('http://static9.cdn.ubi.com/ru-RU/images/2014.08.13%20-%20Portal680-%20Heroes%20VIItcm48165081.jpg')
from PIL import Image
from StringIO import StringIO
i = Image.open(StringIO(ri.content))
print(i)
'''