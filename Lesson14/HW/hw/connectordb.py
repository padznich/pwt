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


    def insert_into_money_table (self, *args):
        '''
        Enter:
         id=int
         currency='str'
         value=int
         player_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "INSERT INTO `money` (`id`, `currency`, `value`, `created`, `updated`, `players_id`)" \
                            " VALUES (%(arg0)s, %(arg1)s, %(arg2)s, now(), now(), %(arg3)s);"
                sql_data = {"arg0": args[0],
                            "arg1": args[1],
                            "arg2": args[2],
                            "arg3": args[3]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()

    def insert_into_counters_table (self, *args):
        '''
        Enter:
         id=int
         counter_name='str'
         value=int
         player_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "INSERT INTO `counters` (`id`, `counter_name`, `value`, `created`, `updated`, `players_id`)" \
                            " VALUES (%(arg0)s, %(arg1)s, %(arg2)s, now(), now(), %(arg3)s);"
                sql_data = {"arg0": args[0],
                            "arg1": args[1],
                            "arg2": args[2],
                            "arg3": args[3]}

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
         player_id=int
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
                            " VALUES (%(arg0)s, %(arg1)s, %(arg2)s, %(arg3)s, now(), now(), %(arg4)s);"
                sql_data = {"arg0": args[0],
                            "arg1": args[1],
                            "arg2": args[2],
                            "arg3": args[3],
                            "arg4": args[4]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()


    def update_money_table (self, *args):
        '''
        Enter
         value=int
         currency='str'
         player_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "UPDATE `money`" \
                            " SET `value`=%(arg0)s, `updated`=now()" \
                            " WHERE `currency`=%(arg1)s AND `id`=%(arg2)s;"
                sql_data = {"arg0": args[0],
                            "arg1": args[1],
                            "arg2": args[2]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()

    def update_counters_table (self, *args):
        '''
        Enter
         value=int
         counter_name='str'
         player_id=int
        '''
        try:
            self.connection = MySQLdb.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            with self.connection:
                cursor = self.connection.cursor()

                sql_query = "UPDATE `counters`" \
                            " SET `value`=%(arg0)s, `updated`=now()" \
                            " WHERE `counter_name`=%(arg1)s AND `id`=%(arg2)s;"
                sql_data = {"arg0": args[0],
                            "arg1": args[1],
                            "arg2": args[2]}

                cursor.execute(sql_query, sql_data)
        finally:
            self.connection.close()


if __name__ == '__main__':
    c = Connect('localhost', 'pad', 'padznich', 'hw14')
    # c.insert_into_money_table(3, 'GBH', 57, 1)
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

    c.show_table('session')