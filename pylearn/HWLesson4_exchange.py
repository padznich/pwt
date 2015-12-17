# coding=utf-8

import urllib2
import xml.dom.minidom

def get_rub(date):
    #http://www.nbrb.by/Services/XmlExRates.aspx?ondate=01/31/2011
    urlic = r'http://www.nbrb.by/Services/XmlExRates.aspx?ondate={}'.format(date)
    page = urllib2.urlopen(urlic)
    page.getcode()
    content = page.read()
    page.close()

    dom = xml.dom.minidom.parseString(content)
    rate_tag = dom.getElementsByTagName("Rate")[17].childNodes[0]

    return(float(rate_tag.nodeValue))

if __name__ == '__main__':
    print(get_rub('01/31/2011'))