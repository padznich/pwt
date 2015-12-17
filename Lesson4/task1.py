s = 'C:\windows\system32\drivers\etc\hosts'

with open(s, 'r') as file:
    count1 = 0
    sl = set()
    for line in file:
        count1 += 1
        sl.add(line)
    count2 = len(sl)
    print('Number of strings in the file {} :'.format(count1))
    print('Number of exlusive strings in the file {} :'.format(count2))