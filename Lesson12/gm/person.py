# coding=utf-8

import json

from gm import counters
from gm import money
from gm import session


class Player(object):

    def __init__(self, plr_name, plr_login, email, password):
        self.plr_name = plr_name
        self.plr_login = plr_login
        self.email = email
        self.password = password

        self.money = money.Money(self.plr_name)
        self.session = session.Session(self.plr_name)
        self.counter1 = counters.Counters()
        self.counter2 = counters.Counters()
        self.counter3 = counters.Counters()

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "plr_name": self.plr_name,
            "plr_login": self.plr_login,
            "email": self.email,
            "password": self.password,
            "money": self.money,
            "session": self.session,
            "counter1": self.counter1,
            "counter2": self.counter2,
            "counter3": self.counter3,
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.plr_name = object_as_dict["plr_name"]
        self.plr_login = object_as_dict["plr_login"]
        self.email = object_as_dict["email"]
        self.password = object_as_dict["password"]
        self.money = object_as_dict["money"]
        self.session = object_as_dict["session"]
        self.counter1 = object_as_dict["counter1"]
        self.counter2 = object_as_dict["counter2"]
        self.counter3 = object_as_dict["counter3"]
        return object_as_dict


    def login(self, t_login='', t_password=''):

        t_login = input('Enter login \n')
        if t_login != self.login:
            print("Wrong login")
            return self.login()

        t_password = input('Enter password \n')
        if t_password != self.password:
            print("Wrong password")
            return self.login(t_login)

        print("Welcome {}".format(self.plr_name))
        self.load(open('savefile.json', 'r'))
        self.session.__enter__()

    def logout(self):

        print("Bye-bye {}".format(self.plr_name))
        self.session.__exit__()
        self.save(open('savefile.json', 'w'))



    def say(self):
        print("I'm a simple Player.")

    def run(self):
        print("I run. My speed is 7 kilometers per hour")

    def stop(self):
        print("I've stopped!")


    def __str__(self):
        return "{}(name='{}')".format(self.__class__.__name__, self.plr_name)

class Moderator(Player):

    def __init__(self, plr_name='Moderator', plr_login='log', email='email', password='pass'):
        Player.__init__(self, plr_name, plr_login, email, password)

    def say(self):
        print("I'm a moderator.")

    def run(self):
        print("My speed is 10 kilometers per hour")

class Admin(Moderator):

    def __init__(self, plr_name='Admin', plr_login='log', email='email', password='pass'):
        Player.__init__(self, plr_name, plr_login, email, password)

    def say(self):
        print("I'm an administrator.")

    def run(self):
        print("My speed is 50 kilometers per hour")
