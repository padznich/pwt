# coding=utf-8


'''
def empty_row(file_name):
    with open(file_name, 'r') as file:
        list_rows = file.readlines()
    sum = 0
    for row in list_rows:
        if row == '\n':
            sum += 1
    # if last row is empty, it means that previous row ends with '\n'
    if list_rows[len(list_rows) - 1][-1] == '\n':
        sum += 1
    out = sum
    return out

if __name__ == '__main__':
    print(empty_row('file_name.txt'))
'''

a1 = range(2, 15, 2)
a2 = map(lambda x: chr(x + 95), a1)
D = dict(zip((a2), (a1)))

print(D.get('a', 1))
print(D.setdefault('b', 9))
print('---',D['b'])

print(sorted(D.values()))
print(sorted(D.keys()))



'''
# Use the __getitem__ method as the key function
sorted(numbers, key=numbers.__getitem__)
# In order of sorted values: [1, 2, 3, 4]
['first', 'second', 'third', 'Fourth']
'''