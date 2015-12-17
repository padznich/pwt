# coding=utf-8

import argparse
import urllib2
import xml.dom.minidom

parser = argparse.ArgumentParser()
'''
--path c:\Users\projects\pylearn\
--file Lesson4taskcar_stats.csv
'''
parser.add_argument("--path", type=str, required=True, help="Enter folder path to csv file.")
parser.add_argument("--file", type=str, required=True, help="Enter csv file name.")
args = parser.parse_args()

with open('{}{}'.format(args.path, args.file), 'r') as file:
    if file.mode == 'r':
        flines = file.readlines()

#
# number of useful lines in the file
#
useful_lines_number = 0
for i in range(1, len(flines)):
    if not (flines[i].split(',')[0]):
        break
    useful_lines_number += 1
'''
print('DEBUG: lines number', lines_number)
print('DEBUG: line 1', flines[1].split(','))
print('DEBUG: line 52', flines[lines_number].split(','))
'''


#
# get exchange RUB
#
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


#
# Total amount of  money
#
def spent_money():
    outsum = 0
    try:
        for i in range(1, useful_lines_number + 1):
            if flines[i].split(',')[5] == 'BYR':
                outsum += float(flines[i].split(',')[3])
            elif flines[i].split(',')[5] == 'RUR':
                outsum += float(flines[i].split(',')[3]) * get_rub(flines[i].split(',')[0])
    except Exception as e:
        with open('file.log', 'a+') as file:
                file.write('Total amount of money\n')
                file.write('{}\n'.format(e))
    return(outsum)


#
# Average costs per the month
#
def costs_per_month():
    dict1 = {}
    for i in range(1, 13):
        dict1[i] = 0

    for i in range(1, useful_lines_number + 1):
        try:
            month = (flines[i].split(',')[0])
            month = int(month.split('/')[0])
            dict1[month] += float(flines[i].split(',')[3])
        except Exception as e:
            with open('file.log', 'a+') as file:
                file.write('Average amount of money spent per the month\n')
                file.write('{}\n'.format(e))
    return(spent_money() / len(dict1.keys()))


#
# Average consumption per 100 km
#
def consumption():
    mileage_base = float(flines[1].split(',')[1])
    mileage_out = float(flines[useful_lines_number].split(',')[1])
    mileage = mileage_out - mileage_base

    litres = 0
    for i in range(1, useful_lines_number + 1):
        try:
            litres += float(flines[i].split(',')[3]) / float(flines[i].split(',')[4])
            if float(flines[i].split(',')[3]) / float(flines[i].split(',')[4]) > 50:
                print('Somethig gone wrong!')
        except Exception as e:
            with open('file.log', 'a+') as file:
                file.write('Average consumption per 100 km\n')
                file.write('{}\n'.format(e))

    base_tank = float(flines[1].split(',')[2])
    out_tank = float(flines[useful_lines_number].split(',')[2])

    litres = litres + base_tank - out_tank
    return(litres * 100 / mileage)

if __name__ == '__main__':
    print(u'1. Total spent money: {:.0f} BYR'.format(spent_money()))
    print(u'2. Average spent money per month: {:.0f} BYR'.format(costs_per_month()))
    print(u'3. Average consumption {:.2f} litres per 100 km.'.format(consumption()))