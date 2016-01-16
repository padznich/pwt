# coding=utf-8

import MySQLdb
import datetime
import time

class Connect:
    '''
    Connecting to the MySQL DataBase:

        localhost
        user
        user_password
        db_name
    '''
    def __init__(self, host, user, password, db):
        '''
        Enter:
        :param host:
        :param user:
        :param password:
        :param db:
        '''
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def show_table(self, table_name):
        '''
        Enter
          table_name='str'
        '''
        self.connection = MySQLdb.connect(self.host,
                                          self.user,
                                          self.password,
                                          self.db)
        with self.connection:

            cursor = self.connection.cursor()

            sql_query = "SELECT * FROM " + table_name

            cursor.execute(sql_query)
            print(format(table_name, '_^110'))
            for row in cursor:
                print(row)
            print('/' * 110)


    def insert_into_players_table (self, *args):
        '''
        Enter:
         id=int
         plr_name='str'
         plr_login='str'
         email='str'
         password='str'
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "INSERT INTO `players` (`id`, `plr_name`, `plr_login`, `email`, `password`," \
                            " `created`, `updated`)" \
                            " VALUES (%(id)s, %(plr_name)s, %(plr_login)s, %(email)s, %(password)s," \
                            " now(), now());"
                sql_data = {"id": args[0],
                            "plr_name": args[1],
                            "plr_login": args[2],
                            "email": args[3],
                            "password": args[4]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()

    def insert_into_money_table (self, *args):
        '''
        Enter:
         id=int
         currency='str'
         value=int
         players_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "INSERT INTO `money` (`id`, `currency`, `value`, `created`, `updated`, `players_id`)" \
                            " VALUES (%(id)s, %(currency)s, %(value)s, now(), now(), %(players_id)s);"
                sql_data = {"id": args[0],
                            "currency": args[1],
                            "value": args[2],
                            "players_id": args[3]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()

    def insert_into_counters_table (self, *args):
        '''
        Enter:
         id=int
         counter_name='str'
         value=int
         players_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "INSERT INTO `counters` (`id`, `counter_name`, `value`, `created`, `updated`, `players_id`)" \
                            " VALUES (%(id)s, %(counter_name)s, %(value)s, now(), now(), %(players_id)s);"
                sql_data = {"id": args[0],
                            "counter_name": args[1],
                            "value": args[2],
                            "players_id": args[3]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()

    def insert_into_session_table (self, *args):
        '''
        Enter:
         id=int
         start_time=DATETIME
         finish_time=DATETIME
         total_time=TIME
         players_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "INSERT INTO `session` (`id`, `start_time`, `finish_time`, `total_time`," \
                            " `created`, `updated`, `players_id`)" \
                            " VALUES (%(id)s, %(start_time)s, %(finish_time)s, %(total_time)s, now(), now()," \
                            " %(players_id)s);"
                sql_data = {"id": args[0],
                            "start_time": args[1],
                            "finish_time": args[2],
                            "total_time": args[3],
                            "players_id": args[4]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()


    def update_money_table (self, *args):
        '''
        Enter
         value=int
         currency='str'
         players_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "UPDATE `money`" \
                            " SET `value`=%(value)s, `updated`=now()" \
                            " WHERE `currency`=%(currency)s AND `players_id`=%(players_id)s;"
                sql_data = {"value": args[0],
                                "currency": args[1],
                                "players_id": args[2]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()

    def update_counters_table (self, *args):
        '''
        Enter
         value=int
         counter_name='str'
         players_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "UPDATE `counters`" \
                            " SET `value`=%(value)s, `updated`=now()" \
                            " WHERE `counter_name`=%(counter_name)s AND `players_id`=%(players_id)s;"
                sql_data = {"value": args[0],
                            "counter_name": args[1],
                            "players_id": args[2]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()


    def load_player_db(self, *args):
        '''
        Returns player's arguments.
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()
                sql_query = "SELECT * FROM players WHERE id=%(id)s"
                sql_data = {"id": args[0]}
                cursor.execute(sql_query, sql_data)
            for w in cursor:
                self.id = w[0]
                self.plr_name = w[1]
                self.plr_login = w[2]
                self.email = w[3]
                self.password = w[4]
        finally:
            self.connection.close()
        return self.id, self.plr_name, self.plr_login, self.email, self.password

    def load_money_db(self, *args):
        '''
        Returns players arguments.
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()
                sql_query = "SELECT * FROM money WHERE players_id=%(id)s"
                sql_data = {"id": args[0]}
                cursor.execute(sql_query, sql_data)
                l_wallet = {}

            for w in cursor:
                l_wallet[w[1]] = w[2]
        finally:
            self.connection.close()
        return l_wallet



if __name__ == '__main__':
    c = Connect('localhost', 'pad', 'padznich', 'hw14')
    #c.insert_into_money_table(1, 'GBH', 57, 1)
    # c.insert_into_counters_table(2, 'words', 389, 1)

    # a = datetime.datetime.now()
    # time.sleep(5.7)
    # b = datetime.datetime.now()
    # c.insert_into_session_table(3, a, b, b - a, 1 )

    # c.show_table('money')
    # c.update_money_table(34, 'BLR', 1)
    # c.show_table('money')

    # c.show_table('counters')
    # c.update_counters_table(2876, 'steps', 1)
    # c.show_table('counters')

    c.load_player_db(1)
    c.load_money_db(1)