# coding=utf-8

import connectordb

class Counters(object):

    def __init__(self, players_id):

        self.players_id = players_id
        self.counters_dict = {}   # {counter_name : value, }

        self.db = connectordb.db_connect

    def show_score(self):
        print("Player id : {}. counters_dict:".format(self.players_id))
        for k in self.counters_dict.keys():
            print("For {} value is: {}".format(k, self.counters_dict[k]))

    def rob(self, name, value):
        print("Player id: {}. Counter {} decreased with {}.".format(self.players_id, nmae, value))
        self.counters_dict.setdefault(name, 0)
        self.counters_dict[name] -= value

    def add(self, name, value):
        print("Player id: {}. Counter {} increased with {}.".format(self.players_id, name, value))
        self.counters_dict.setdefault(name, 0)
        self.counters_dict[name] += value



    def load_from_db(self):
        '''
        Returns counter.
        '''
        sql_query = "SELECT * FROM counters WHERE players_id=%(players_id)s"
        sql_data = {"players_id": self.players_id}
        data = self.db.run_query(sql_query, sql_data)
        for w in data:
            self.counters_dict[w[1]] = w[2]

    def save_to_db(self, id, counter_name, value):
        '''
        All counter_name must have unique id.
        '''
        try:
            sql_query = "INSERT INTO counters (id, counter_name, value, created, updated, players_id)" \
                        " VALUES (%(id)s, %(counter_name)s, %(value)s, now(), now(), %(players_id)s);"
            sql_data = {"id": id,
                        "counter_name": counter_name,
                        "value": value,
                        "players_id": self.players_id}
            self.db.run_query(sql_query, sql_data)

        except Exception as er:
            print(er)
            sql_query = "UPDATE counters" \
                        " SET value=%(value)s, updated=now()" \
                        " WHERE counter_name=%(counter_name)s AND players_id=%(players_id)s;"
            sql_data = {"value": value,
                        "counter_name": counter_name,
                        "players_id": self.players_id}
            self.db.run_query(sql_query, sql_data)

    def delete_from_db(self, id):
        sql_query = "DELETE FROM counters" \
                    " WHERE  id=%(id)s;"
        sql_data = {"id": id}
        self.db.run_query(sql_query, sql_data)


if __name__ == '__main__':

    c = Counters(1)
    c.show_score()
    c.load_from_db()
    c.show_score()

    c.save_to_db(3, 'some', 787)
    c.show_score()
    c.delete_from_db(3)


