import urllib2
from bs4 import BeautifulSoup


def GetRUR():
    s = 'http://nbrb.by/statistics/Rates/RatesDaily.asp'
    u = urllib2.urlopen(s)
    u.getcode()
    contents = u.read()
    u.close()

    soup = BeautifulSoup(contents, 'html.parser')
    CURRENTS = soup.find('table', id='BodyHolder_gvMain')
    CUR = CURRENTS('td')[44].string
    CUR = CUR.strip()
    CUR = CUR.replace(',', '.')
    CUR = float(CUR)

    return(CUR)

if __name__ == '__main__':
    print(GetRUR())