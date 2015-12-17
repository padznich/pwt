data = ((1,1,1),
        (1,1,1),
        (1,1,1),)
arg1 = 0
arg2 = 0

def count_neighbours(data, arg1, arg2):
    out = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if data[arg1 + i][arg2 + j] == 1 and arg1 + i >= 0 and arg2 + j >= 0:
                    out += 1
            except:
                continue
    if data[arg1][arg2] == 1:
        out = out - 1
    return(out)

print(count_neighbours(data, arg1, arg2))