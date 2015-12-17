#l1 = ["s", "sp", "s", "spr", "sp", "s", "sp", "a"]
#l1 = []
l1 = input()
if l1 ==[]:
    print('[]')
else:
    l2 = []
    l2.append( l1[0])
    s = set(l1[0])

    for i in range(len(l1)-1):
        if l1[i + 1] not in s:
            s.add(l1[i+1])
            l2.append(l1[i+1])
    print(l2)