data = [1, 2, 3, 5, 6]


def median(data):
    data.sort()
    ld = len(data)
    if ld % 2 != 0:
#ODD NUMBER OF ELEMENTS
        pos = int(ld / 2)
        out = data[pos]

    elif ld % 2 == 0:
#EVEN NUMBER OF ELEMENTS
        left = data[int(ld / 2 - 1)]
        right = data[int(ld / 2)]

        if (left + right) % 2 == 0:
            out = int((left + right) / 2)
        else:
            out = (left + right) / 2
    return (out)

print(median(data))