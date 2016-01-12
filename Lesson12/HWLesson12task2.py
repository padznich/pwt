# coding=utf-8

from time import sleep
import os.path
import sys

path_to_module = os.path.split(__file__)[0]
sys.path.append(path_to_module)

def reload_player():

    while 1:
        prev_value = os.path.getmtime(r'./gm/person.py')
        sleep(1)

        from gm import person
        current_value = os.path.getmtime(r'./gm/person.py')

        if current_value != prev_value:
            print("DEBUG: made changes in module person")
            reload(person)

#DEBUG: print(path.getmtime(r'C:/home/pwt/Lesson12/gm/person.py'))

if __name__ == '__main__':
    reload_player()