'''
#
# raise Exception
#
def take_beer(fridge, number=1):
    if "beer" not in fridge:
        raise Exception("No more beer:(")

    if number > fridge["beer"]:
        raise Exception("Not enough beer:(")

    fridge["beer"] -= number

if __name__ == '__main__':
    fridge = {}
    fridge["beer"] = 6
    print(fridge)
    take_beer(fridge, 7)
    print(fridge)
'''
'''
#
# Debugger
#

def multiple(*numbers):
    i = 0
    res = 1
    while i <= len(numbers):
        res = numbers[i] * res

if __name__ == "__main__":
    multiple(1, 2, 3, 4)
'''
