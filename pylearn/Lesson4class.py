'''
s = 'C:\\home\\Lesson4\\hello.txt'
#s = r'C:\home\Lesson4\hello.txt'
#s = ''


with open(s, 'a+') as file:
    #print(file.read())
    file.write('\nspam')
    file.write('\nspam2')
    file.write('\nspam3')
'''



import os

for root_dir, dirs, files in os.walk("."):
    print("root_dir is {}, dirs are {}, files are {}".format(root_dir, dirs, files))