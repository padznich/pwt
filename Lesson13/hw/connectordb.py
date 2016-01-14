# coding=utf-8
'''
CREATE TABLE `players` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `plr_name` varchar(40) COLLATE utf8_bin NOT NULL,
    `plr_login` varchar(40) COLLATE utf8_bin NOT NULL UNIQUE,
    `email` varchar(40) COLLATE utf8_bin NOT NULL UNIQUE,
    `password` varchar(40) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

CREATE TABLE `player_money` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `currency` varchar(40) COLLATE utf8_bin,
    `value` INT,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

CREATE TABLE `player_session` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `start_time` DATETIME,
    `finish_time` DATETIME,
    `total_time, sec` INT,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

CREATE TABLE `player_counters` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `counter_name` varchar(40) COLLATE utf8_bin,
    `value` INT,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
'''

import pymysql
import pymysql.cursors

class Connect:
    '''
    Making DataBase with MySQL.
    '''
    def __init__(self, host, user, password, db):

        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def add_to_db(self, table_name, *args):
        '''
        Function fill the last row of the table.
        '''
        try:
            self.connection = pymysql.connect(host=self.host,
                                              user=self.user,
                                              password=self.password,
                                              db=self.db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor
                                              )
            with self.connection.cursor() as cursor:
                sql = "SELECT id FROM {table_name};".format(table_name=table_name)
                cursor.execute(sql)
                new_row_pos = len([le for le in cursor]) + 1
                lt = list(args)
                lt.insert(0, new_row_pos)
                args = tuple(lt)

                cursor.execute("INSERT INTO {table_name} ()"
                               " VALUES {args};".format(table_name=table_name,
                                                        args=args
                                                        )
                               )
                self.connection.commit()
        finally:
            self.connection.close()

    def change_value(self, table_name, row_name='', value=0, number_of_rows=1, column_name='value'):
        try:
            self.connection = pymysql.connect(host=self.host,
                                              user=self.user,
                                              password=self.password,
                                              db=self.db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor
                                              )

            row_to_change = 'counter_name' if table_name == 'player_counters' else 'currency'

            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE {table_name}"
                               " SET `{column_name}`={value}"
                               " WHERE (`{row_to_change}`)='{row_name}'"
                               " LIMIT {n};".format(table_name=table_name,
                                                    column_name=column_name,
                                                    value=value,
                                                    row_to_change=row_to_change,
                                                    row_name=row_name,
                                                    n=number_of_rows
                                                    )
                               )
                self.connection.commit()
        finally:
            self.connection.close()

    def show_db(self, table_name):
        try:
            self.connection = pymysql.connect(host=self.host,
                                              user=self.user,
                                              password=self.password,
                                              db=self.db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor
                                              )
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM {table_name};".format(table_name=table_name)
                cursor.execute(sql)
                #result = cursor.fetchall()
                for row in [le.values() for le in cursor]:
                    print(row)
        finally:
            self.connection.close()




    if __name__ == '__main__':
        c = Connect('localhost', 'pad', 'padznich', 'pad_test')
        c.change_value('player_counters', 'de', 1)
        #c.add_to_db('player_counters', 'de', 6748132)
    c.show_db('player_counters')

