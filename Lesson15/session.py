# coding=utf-8

import datetime

import connectordb

class Session(object):

    def __init__(self, players_id):

        self.players_id = players_id
        self.currrent_session_info = [] # [start, finish, total]

        self.db = connectordb.db_connect

    def _start(self):
        self.start = datetime.datetime.now()
        self.currrent_session_info.append(self.start)
        print("Session started.")

    def _finish(self):
        self.finish = datetime.datetime.now()
        self.currrent_session_info.append(self.finish)

        self.total = self.finish - self.start
        self.currrent_session_info.append(self.total)
        print("Session finished")

    def show_info(self):
        print("For player_id {}.".format(self.players_id))
        print("Session started at {}.".format(self.currrent_session_info[0]))
        print("Session finished at {}.".format(self.currrent_session_info[1]))
        print("Total session time is {}".format(self.currrent_session_info[2]))



    def load_from_db(self):
        '''
        Returns session_info.
        '''
        sql_query = "SELECT * FROM session WHERE players_id=%(players_id)s"
        sql_data = {"players_id": self.players_id}
        data = self.db.run_query(sql_query, sql_data)
        for w in data:
            self.currrent_session_info.append([w[1], w[2], w[3]])

    def save_to_db(self, id, start_time, finish_time, total_time):
        '''
        All sessions must have unique id.
        '''
        try:
            sql_query = "INSERT INTO session (id, start_time, finish_time, total_time, created, updated, players_id)" \
                        " VALUES (%(id)s, %(start_time)s, %(finish_time)s, %(total_time)s, now(), now()," \
                        " %(players_id)s);"
            sql_data = {"id": id,
                        "start_time": start_time,
                        "finish_time": finish_time,
                        "total_time": total_time,
                        "players_id": self.players_id}
            self.db.run_query(sql_query, sql_data)
        except Exception as er:
            print(er)

    def delete_from_db(self, id):
        sql_query = "DELETE FROM session" \
                    " WHERE  id=%(id)s;"
        sql_data = {"id": id}
        self.db.run_query(sql_query, sql_data)




if __name__ == '__main__':

    s = Session(1)
    s._start()
    s._finish()

    s.show_info()

    s.load_from_db()
    s.show_info()

    s.save_to_db(4, datetime.datetime.now(), datetime.datetime.now(), 0)