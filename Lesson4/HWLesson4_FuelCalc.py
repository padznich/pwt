from os import path
import HWLesson4_nbrb # returns float(RUR) coast exchange


file_loc = path.split(path.realpath('Lesson4taskcar_stats.csv'))
Path = file_loc[0]
File = file_loc[1]

with open(File, 'r') as file:
    if file.mode == 'r':
        flines = file.readlines()

#
# Total amount of  money
#
outsum = 0
for i in range(1, len(flines)):
    if flines[i].split(',')[5] == 'BYR':
        outsum += float(flines[i].split(',')[3])
    elif flines[i].split(',')[5] == 'RUR':
        outsum += float(flines[i].split(',')[3]) * HWLesson4_nbrb.GetRUR()
print(u'1. Total spent money: {:.0f} BYR'.format(outsum))

#
# Average amount of money spent per the month
#
dict1 = {}
for i in range(1, 13):
    dict1[i] = 0
for i in range(1, len(flines)):
    try:
        month = (flines[i].split(',')[0])
        month = int(month.split('/')[0])
        dict1[month] += float(flines[i].split(',')[3])
        out_tank = float(flines[i].split(',')[2])
    except:
        break
print(u'2. Average spent money per month: {:.0f} BYR'.format(outsum / len(dict1.keys())))

#
# Average consumption per 100 km
#
mileage1 = float(flines[1].split(',')[1])
dict2 = {}
for i in range(1, len(flines)):
    try:
        dict2[int(flines[i].split(',')[1])] = None
    except:
        dict2[None] = None
mileage2 = max(dict2.keys())

mileage = mileage2 - mileage1

litres = 0
for i in range(1, len(flines)):
    try:
        litres += float(flines[i].split(',')[3]) / float(flines[i].split(',')[4])
        if float(flines[i].split(',')[3]) / float(flines[i].split(',')[4]) > 50:
            print('Somethig gone wrong!')
    except:
        break

base_tank = float(flines[1].split(',')[2])

litres = litres + base_tank - out_tank # out_tank look at line 35
print(u'3. Average consumption {:.2f} litres per 100 km.'.format((litres * 100) / mileage))