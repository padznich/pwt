
from bs4 import BeautifulSoup
import urllib2

file = 'script.html'
sock = urllib2.urlopen('https://dev.projectoxford.ai/docs/services/5639d931ca73072154c1ce89/operations/563b31ea778daf121cc3a5fa/console')
sock.getcode()
data = sock.read()
sock.close()

soup = BeautifulSoup(data, 'html.parser')

#import pprint
#pprint.pprint(soup.find_all('script')[18])
#pprint.pprint(soup.body.ul.find_all('a'))

with open(file, 'w') as html:
    html.write(soup.find_all('script')[18]) # soup.find_all('script')[23])
