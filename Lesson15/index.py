# coding=utf-8

import time

from hw import person


p1 = person.Player(1, 'Bob', 'akhalai', 'bob@mail.ru', 'pass1')
p2 = person.Moderator(1)
p3 = person.Admin(1)



if __name__ == '__main__':
    print(p1.plr_name)
    p1.session._start()
    p1.money.add('RUB', 500)
    p1.money.show_wallet()
    p1.money.rob('RUB', 200)
    p1.money.add('USD', 900)
    p1.money.show_wallet()
    time.sleep(0.4)
    p1.session._finish()
    time.sleep(0.2)
    p1.session._start()
    time.sleep(0.1)
    p1.session._finish()
    p1.session.show_info()

    p1.counter.add('steps', 20)
    p1.counter.show_score()
    p1.counter.rob('steps', 3)
    p1.counter.show_score()

    p1.say()
    p2.say()
    p3.say()

    print(p3)

    print("DEBUG: loading from db for Player", "@" * 30)
    p4 = person.Player(1)
    p4.load_from_db()
    p4.money.show_wallet()
    p4.counter.show_score()
    print(p4.session_info)

    print("DEBUG: load from db for Moderator",'#' * 30)
    p2.load_from_db()
    p2.money.show_wallet()
    p2.counter.show_score()
    print(p2.session_info)

    print("DEBUG: load from db for Administrator",'^' * 30)
    p3.load_from_db()
    p3.money.show_wallet()
    p3.counter.show_score()
    print(p3.session_info)