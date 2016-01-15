# coding=utf-8

import json
import pickle


import counters
import money
import session
import lister
import connectordb

class Player(lister.ListTree):

    def __init__(self, plr_name, plr_login, email, password):

        self.plr_name = plr_name
        self.plr_login = plr_login
        self.email = email
        self.password = password

        self.money = money.Money(self.plr_name)
        self.session = session.Session(self.plr_name)
        self.counter1 = counters.Counters(name='counter1')
        self.counter2 = counters.Counters(name='counter2')
        self.counter3 = counters.Counters(name='counter3')

    def as_dict(self):
        '''
        Information that will get to the DataBases.
        '''
        d = {
            "type": self.__class__.__name__,
            "plr_name": self.plr_name,
            "plr_login": self.plr_login,
            "email": self.email,
            "password": self.password,
            "money_wallet": self.money.wallet,
            "money_deals": self.money.money_deals,
            "session_info": self.session.session_info,
            "counter1": self.counter1.counter,
            "counter2": self.counter2.counter,
            "counter3": self.counter3.counter,
        }
        return d

    def save(self, f_name='saved_db'):
        '''
        Pickle save. As default saving.
        '''
        try:
            with open(f_name, 'wb') as f:
                pickle.dump(self.as_dict(), f)
        except Exception as ex:
            print(ex)
        print("Saved in {}.".format(f_name))

    def save_json(self, f_name='saved_db_json'):
        '''
        Json save. For cheaters.
        '''
        try:
            with open(f_name, 'wb') as f:
                json.dump(self.as_dict(), f)
        except Exception as ex:
            print(ex)
        print("Saved as json in {}.".format(f_name))

    def load(self, f_name='saved_db'):
        '''
        Pickle load. As default loading.
        '''
        try:
            with open(f_name, 'rb') as f:
                data = pickle.load(f)
            self.plr_name = data["plr_name"]
            self.plr_login = data["plr_login"]
            self.email = data["email"]
            self.password = data["password"]
            self.money.wallet = data["money_wallet"]
            self.money.money_deals = data["money_deals"]
            self.session.session_info = data["session_info"]
            self.counter1.counter = data["counter1"]
            self.counter2.counter = data["counter2"]
            self.counter3.counter = data["counter3"]
        except Exception as ex:
            print(ex)
        print("Loaded successful from {}.".format(f_name))

    def load_json(self, f_name='saved_db_json'):
        '''
        Json load. For cheaters.
        '''
        try:
            object_as_dict = json.load(f_name)
            self.plr_name = object_as_dict["plr_name"]
            self.plr_login = object_as_dict["plr_login"]
            self.email = object_as_dict["email"]
            self.password = object_as_dict["password"]
            self.money.wallet = object_as_dict["money_wallet"]
            self.money.money_deals = object_as_dict["money_deals"]
            self.session.session_info = object_as_dict["session_info"]
            self.counter1.counter = object_as_dict["counter1"]
            self.counter2.counter = object_as_dict["counter2"]
            self.counter3.counter = object_as_dict["counter3"]
        except Exception as ex:
            print(ex)

        print('Loaded json successful from {}.'.format(f_name))

    def login(self, t_login='', t_password=''):
        '''
        Login function as a default carry out pickle.
        '''
        if t_login != self.plr_login:
            if self.plr_login != raw_input('Enter login: '):
                print("Wrong login")
                return self.login()

        if self.password != raw_input('Enter password: '):
            print("Wrong password")
            return self.login(self.plr_login)

        print("Welcome {}".format(self.plr_name))
        self.load()
        self.session.__enter__()

    def logout(self):
        '''
        Logout function as a default carry out pickle.
        '''
        self.session.__exit__()
        self.save("{}'s logout_save".format(self.plr_login))
        print("Bye-bye {}".format(self.plr_name))



    def say(self):
        print("I'm a simple Player.")

    def run(self):
        print("I run. My speed is 7 kilometers per hour")

    def stop(self):
        print("I've stopped!")

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


if __name__ == '__main__':

    p = Admin()
    print(p.as_dict())
    print(p)