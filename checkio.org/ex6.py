data = [
    "OOX",
    "XXO",
    "OXX"]
#                    shame on me
def checkio(data):
    sXh = 0
    sOh = 0
    sXv = 0
    sOv = 0
    sXdr = 0
    sOdr = 0
    sXdl = 0
    sOdl = 0
    out = ''
    for i in range(3):
# diagonal /
        if data[i][2 - i] == 'X':
            sXdr += 1
        elif data[i][2 - i] == 'O':
            sOdr += 1
# diagonal \
        if data[i][i] == 'X':
            sXdl += 1
        elif data[i][i] == 'O':
            sOdl += 1


        for j in range(3):
# in row
            if data[i][j] == 'X':
                sXh += 1
            elif data[i][j] == 'O':
                sOh += 1
# in column
            if data[j][i] == "X":
                sXv += 1
            elif data[j][i] == "O":
                sOv += 1
        if sXh == 3 or sXv == 3:
            out = 'X'
            break
        else:
            sXh, sXv = 0, 0

        if sOh == 3 or sOv == 3:
            out = 'O'
            break
        else:
            sOh, sOv = 0, 0
    if sXdr == 3 or sXdl == 3:
        out = 'X'
    elif sOdr == 3 or sOdl == 3:
        out = 'O'
    if out == '':
        out = 'D'
    return(out)

print(checkio(data))