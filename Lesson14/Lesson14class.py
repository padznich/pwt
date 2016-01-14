# coding=utf-8

import MySQLdb

class Connect:
    '''
    Making DataBase with MySQL.
    '''
    def __init__(self, host, user, password, db):

        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def show_table(self, table_name):

        self.connection = MySQLdb.connect(self.host,
                                          self.user,
                                          self.password,
                                          self.db)
        with self.connection:

            cursor = self.connection.cursor()

            sql_query = "SELECT * FROM " + table_name #%(table_name)s;"
            sql_data = {"table_name": table_name}

            cursor.execute(sql_query, sql_data)

            for row in cursor:
                print(row)


if __name__ == '__main__':
    c = Connect('localhost', 'root', 'root', 'mydb')
    c.show_table('money')

