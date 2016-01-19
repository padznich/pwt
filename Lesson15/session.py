# coding=utf-8

import datetime

import connectordb

class Session(object):

    def __init__(self, players_id):

        self.id = 1
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
        Returns players's sessions to the Player class.
        In Player class as self.session_info = [].
        At the Session class storing only current session information.
        '''
        sql_query = "SELECT * FROM session WHERE players_id=%(players_id)s"
        sql_data = {"players_id": self.players_id}
        data = self.db.run_query(sql_query, sql_data)
        plr_session_info = []
        last_session_in_db = []
        for w in data:
            plr_session_info.append([w[1], w[2], w[3]])
            last_session_in_db = w
        self.id = last_session_in_db[0] + 1

        return plr_session_info

    def save_to_db(self):
        '''
        All sessions must have unique id.
        '''
        try:
            sql_query = "INSERT INTO session (id, start_time, finish_time, total_time, created, updated, players_id)" \
                        " VALUES (%(id)s, %(start_time)s, %(finish_time)s, %(total_time)s, now(), now()," \
                        " %(players_id)s);"
            sql_data = {"id": self.id,
                        "start_time": self.start,
                        "finish_time": self.finish,
                        "total_time": self.total,
                        "players_id": self.players_id}
            self.db.run_query(sql_query, sql_data)
        except Exception as er:
            print(er)

    def delete_from_db(self, id):
        '''
        Delete a session by id.
        '''
        sql_query = "DELETE FROM session" \
                    " WHERE  id=%(id)s;"
        sql_data = {"id": id}
        self.db.run_query(sql_query, sql_data)




if __name__ == '__main__':

    s = Session(1)
    s._start()
    s._finish()

    s.show_info()

    s.save_to_db(4)