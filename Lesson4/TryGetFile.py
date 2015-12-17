import urllib2
from bs4 import BeautifulSoup

urlic = urllib2.urlopen('https://drive.google.com/folderview?id=0B6UbB-lUbcsFQVNqTDdObVZISzA&usp=sharing&tid=0B6UbB-lUbcsFOTB5Q1RHcGl4QVE')
page = urlic.read()
urlic.close()

soup = BeautifulSoup(page, 'html.parser')
link = soup.find('div', id='entry-0B6UbB-lUbcsFMm5pdm5wM1RxdWs')
file = link('div')[5]
#<div class="flip-entry-title">car_stats.csv</div>
print(file)