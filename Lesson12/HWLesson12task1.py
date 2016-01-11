# coding=utf-8

import time
import os
import sys

path_to_module = os.path.split(__file__)[0]
sys.path.append(path_to_module)

from gm import person


p1 = person.Player('Bob', 'akhalai', 'bob@mail.ru', 'pass1')
p2 = person.Moderator()
p3 = person.Admin()


if __name__ == '__main__':
    print(p1.plr_name)
    p1.session.__enter__()
    p1.money.take('RUB', 500)
    p1.money.show_wallet()
    p1.money.give('RUB', 200)
    p1.money.take('USD', 900)
    p1.money.show_wallet()
    time.sleep(0.4)
    p1.session.__exit__()
    time.sleep(0.2)
    p1.session.__enter__()
    time.sleep(0.1)
    p1.session.__exit__()
    p1.session.show_info()

    p1.counter1.add(20)
    p1.counter1.show_score()
    p1.counter1.rob(3)
    p1.counter1.show_score()

    p1.counter2.add(19.7)
    p1.counter2.show_score()
    p1.counter2.rob(5.7)
    p1.counter2.show_score()

    p1.counter3.add(900)
    p1.counter3.show_score()
    p1.counter3.rob(330)
    p1.counter3.show_score()

    p1.say()
    p2.say()
    p3.say()

    p1.login()

    p1.save()
    p1.save('Bob_db')
    p1.logout()
    p1.load()
    p1.load('Bob_db')