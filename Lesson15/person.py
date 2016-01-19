# coding=utf-8

import json
import pickle
import argparse

import counters
import money
import session
import lister
import connectordb

class Player(lister.ListTree):

    def __init__(self, id, plr_name='default', plr_login='default', email='default', password='default'):

        self.id = id
        self.plr_name = plr_name
        self.plr_login = plr_login
        self.email = email
        self.password = password

        self.money = money.Money(self.id)
        self.session = session.Session(self.id)
        self.counter = counters.Counters(self.id)

        self.session_info = []

        self.db = connectordb.db_connect


    def as_dict(self):
        '''
        Information that will get to the DataBases.
        '''
        d = {
            "type": self.__class__.__name__,
            "id": self.id,
            "plr_name": self.plr_name,
            "plr_login": self.plr_login,
            "email": self.email,
            "password": self.password,
            "money_wallet": self.money.wallet,
            "money_deals": self.money.money_deals,
            "session_info": self.session_info,
            "counter": self.counter.counter
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
            self.id = data["id"]
            self.plr_name = data["plr_name"]
            self.plr_login = data["plr_login"]
            self.email = data["email"]
            self.password = data["password"]
            self.money.wallet = data["money_wallet"]
            self.money.money_deals = data["money_deals"]
            self.session_info = data["session_info"]
            self.counter.counter = data["counter"]
        except Exception as ex:
            print(ex)
        print("Loaded successful from {}.".format(f_name))

    def load_json(self, f_name='saved_db_json'):
        '''
        Json load. For cheaters.
        '''
        try:
            object_as_dict = json.load(f_name)
            self.id = object_as_dict["id"]
            self.plr_name = object_as_dict["plr_name"]
            self.plr_login = object_as_dict["plr_login"]
            self.email = object_as_dict["email"]
            self.password = object_as_dict["password"]
            self.money.wallet = object_as_dict["money_wallet"]
            self.money.money_deals = object_as_dict["money_deals"]
            self.session_info = object_as_dict["session_info"]
            self.counter.counter = object_as_dict["counter"]
        except Exception as ex:
            print(ex)

        print('Loaded json successful from {}.'.format(f_name))

    def login(self, t_login='', t_password=''):
        '''
        Login function as a default carry out pickle.
        '''
        if t_login and t_password:
            print('login and password confirmed.')
        print("Welcome {}".format(self.plr_name))
        self.load()
        self.session._start()

    def logout(self):
        '''
        Logout function as a default carry out pickle.
        '''
        self.session._finish()
        self.session_info.append(self.session.currrent_session_info)

        self.save("{}'s logout_save".format(self.plr_login))
        print("Bye-bye {}".format(self.plr_name))


    def load_from_db(self):
        '''
        Returns wallet.
        '''
        sql_query = "SELECT * FROM players WHERE id=%(id)s"
        sql_data = {"id": self.id}
        data = self.db.run_query(sql_query, sql_data)
        for w in data:
            self.id = w[0]
            self.plr_name = w[1]
            self.plr_login = w[2]
            self.email = w[3]
            self.password = w[4]

        self.money.load_from_db()
        self.session_info = self.session.load_from_db()
        self.counter.load_from_db()

    def save_to_db(self):
        '''
        Reestablish the whole player data.

        try - for new player
        except - for updating player's data
        '''
        try:
            sql_query = "INSERT INTO players (id, plr_name, plr_login, email, password, created, updated)" \
                        " VALUES (%(id)s, %(plr_name)s, %(plr_login)s, %(email)s, %(password)s, now(), now());"
            sql_data = {"id": self.id,
                        "plr_name": self.plr_name,
                        "plr_login": self.plr_login,
                        "email": self.email,
                        "password": self.password}
            self.db.run_query(sql_query, sql_data)

            self.session.save_to_db()
            self.money.save_to_db()
            self.counter.save_to_db()

        except Exception as er:
            print(er)

            self.session.save_to_db()
            self.money.save_to_db()
            self.counter.save_to_db()

    def delete_from_db(self, id):
        '''
        Delete a player by id.
        '''
        sql_query = "DELETE FROM players" \
                    " WHERE  id=%(id)s;"
        sql_data = {"id": id}
        self.db.run_query(sql_query, sql_data)


    def say(self):
        print("I'm a simple Player.")

    def run(self):
        print("I run. My speed is 7 kilometers per hour")

    def stop(self):
        print("I've stopped!")


class Moderator(Player):

    def __init__(self, plr_name='Moderator', plr_login='log', email='email', password='pass'):
        Player.__init__(self, id, plr_name, plr_login, email, password)

    def say(self):
        print("I'm a moderator.")

    def run(self):
        print("My speed is 10 kilometers per hour")

class Admin(Moderator):

    def __init__(self, plr_name='Admin', plr_login='log', email='email', password='pass'):
        Player.__init__(self, id, plr_name, plr_login, email, password)

    def say(self):
        print("I'm an administrator.")

    def run(self):
        print("My speed is 50 kilometers per hour")




if __name__ == '__main__':

    p = Player(1)

    p.load_from_db()

    print(p.email)
    print(p.money.show_wallet())
    print(p.session_info)
    print(p.counter.show_score())
