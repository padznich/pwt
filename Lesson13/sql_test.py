# coding=utf-8
'''
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(40) COLLATE utf8_bin NOT NULL,
    `password` varchar(40) COLLATE utf8_bin NOT NULL,
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
    def __init__(self, host, user, password, db,):

        self.connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
    def add_to_db(self, *args, **kwargs):
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
                self.connection.commit()

            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql, ('webmaster@python.org',))
                result = cursor.fetchone()
                print(result)
        finally:
            self.connection.close()



if __name__ == '__main__':
    c = Connect('localhost', 'pad', 'padznich', 'pad_test')
    c.add_to_db()