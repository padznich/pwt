# coding=utf-8

import MySQLdb



class Connect:
    '''
    Connecting to the MySQL DataBase:

        localhost
        user
        user_password
        db_name
    '''
    def __init__(self, host, user, password, db):

        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = MySQLdb.connect(self.host,
                                          self.user,
                                          self.password,
                                          self.db, autocommit=True)

    def run_query(self, sql_query, sql_data):

        cursor = self.connection.cursor()
        cursor.execute(sql_query, sql_data)

        return cursor

db_connect = Connect('localhost', 'root', 'root', 'mydb')

