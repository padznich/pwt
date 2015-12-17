data = [1, 2, 3, 2]

def clear(data):
    c = {}
    for i in range(len(data)):
        c[data[i]] = data.count(data[i])
    print(c)

    list2 = []
    for k, v in c.items():
        if v > 1:
            list2.append(k)
    s = set(list2)

    out_list = []
    for w in data:
        if w in s:
            out_list.append(w)
    return(out_list)

print(clear(data))