data = u"QwErTy911poqqqq"

def checkpass(data):
    lgth = len(data)

    if lgth >= 10:
        supper = 0
        slower = 0
        sint = 0
        for i in range(lgth):
            if data[i].isupper():
                supper = 1
            if data[i].islower():
                slower = 1
            if data[i].isdigit():
                sint = 1
        nice = supper + slower + sint
        if nice == 3:
            return(True)
        else:
            return(False)
    else:
        return(False)

print(checkpass(data))

#def checkio(data):
#    return re.match('^(?=.*[0-9].*)(?=.*[A-Z].*)(?=.*[a-z].*).{10,}$', data) is not None