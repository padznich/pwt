data = 'AAaooo!!!!'

def freq(data):
    import re

    s = data
    s = s.lower()

    list1 = []
    dict1 = {}
    for w in set(s):
        if re.match('[a-z]', w):
            list1.append(s.count(w))
            dict1[w] = s.count(w)
    maxi = max(list1)

    l2 = []
    for k, v in dict1.items():
        if v == maxi:
            l2.append(k)
    out = min(l2)

    return(out)

print(freq(data))
