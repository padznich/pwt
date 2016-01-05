# coding=utf-8

from time import sleep
from os import path

def reload_player():

    while 1:
        prev_value = path.getmtime(r'./gm/person.py')
        sleep(1)

        from gm import person
        current_value = path.getmtime(r'./gm/person.py')

        if current_value != prev_value:
            print("DEBUG: made changes in module person")
            reload(person)

#DEBUG: print(path.getmtime(r'C:/home/pwt/Lesson12/gm/person.py'))

if __name__ == '__main__':
    reload_player()