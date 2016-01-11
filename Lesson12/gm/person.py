# coding=utf-8

# import json
import pickle


import counters
import money
import session



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

    def save(self, f_name='saved_db'):
        try:
            with open(f_name, 'wb') as f:
                pickle.dump(self.as_dict(), f)
        except Exception as ex:
            print(ex)

        # try:
        #     with open('{}_json'.format(f_name), 'wb') as f:
        #         json.dump(self.as_dict(), f)
        # except Exception as ex:
        #     print(ex)

    def load(self, f_name='saved_db'):
        try:
            with open(f_name, 'rb') as f:
                data = pickle.load(f)
            self.plr_name = data["plr_name"]
            self.plr_login = data["plr_login"]
            self.email = data["email"]
            self.password = data["password"]
            self.money = data["money"]
            self.session = data["session"]
            self.counter1 = data["counter1"]
            self.counter2 = data["counter2"]
            self.counter3 = data["counter3"]
        except Exception as ex:
            print(ex)
        print('Loaded successful.')
        # try:
        #     object_as_dict = json.load(file_object)
        #     self.plr_name = object_as_dict["plr_name"]
        #     self.plr_login = object_as_dict["plr_login"]
        #     self.email = object_as_dict["email"]
        #     self.password = object_as_dict["password"]
        #     self.money = object_as_dict["money"]
        #     self.session = object_as_dict["session"]
        #     self.counter1 = object_as_dict["counter1"]
        #     self.counter2 = object_as_dict["counter2"]
        #     self.counter3 = object_as_dict["counter3"]
        # except Exception as ex:
        #     print(ex)


    def login(self, t_login='', t_password=''):

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
        print("Bye-bye {}".format(self.plr_name))
        self.session.__exit__()
        self.save("{}'s logout_save".format(self.plr_login))



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

