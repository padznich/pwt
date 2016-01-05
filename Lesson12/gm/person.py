# coding=utf-8

import json

from gm import counters
from gm import money
from gm import session

class Player(object):

    def __init__(self, plr_name, login, email, password):
        self.name = plr_name
        self.login = login
        self.email = email
        self.password = password

        self.money = money.Money(self.name)
        self.session = session.Session(self.name)
        self.counter1 = counters.Counters()
        self.counter2 = counters.Counters()
        self.counter3 = counters.Counters()


    def say(self):
        print("I'm a simple Player.")

    def run(self):
        print("I run. My speed is 7 kilometers per hour")

    def stop(self):
        print("I've stopped!")


    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "name": self.name
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.name = object_as_dict["name"]
        return object_as_dict

    def __str__(self):
        return "{}(name='{}')".format(self.__class__.__name__, self.name)

class Moderator(Player):

    def __init__(self, plr_name='Moderator', login='log', email='email', password='pass'):
        Player.__init__(self, plr_name, login, email, password)

    def say(self):
        print("I'm a moderator.")

    def run(self):
        print("My speed is 10 kilometers per hour")

class Admin(Moderator):

    def __init__(self, plr_name='Admin', login='log', email='email', password='pass'):
        Player.__init__(self, plr_name, login, email, password)

    def say(self):
        print("I'm an administrator.")

    def run(self):
        print("My speed is 50 kilometers per hour")
