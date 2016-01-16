# coding=utf-8

import connectordb

class Money(object):

    def __init__(self, player_id):

        self.player_id = player_id
        self.wallet = {} # {currency : amount}
        self.money_deals = 0

        self.db = connectordb.db_connect

    def show_wallet(self):
        print("Player id : {}. Wallet:".format(self.player_id))
        for k, v in self.wallet.items():
            print('--{} : {}'.format(k, self.wallet[k]))

    def give(self, cur, val):
        print("{} balance decreased by {} {}.".format(self.player_id, val, cur))
        self.wallet.setdefault(cur, 0)
        self.wallet[cur] -= val
        self.money_deals += 1

    def take(self, cur, val):
        print("{} balance increased by {} {}.".format(self.player_id, val, cur))
        self.wallet.setdefault(cur, 0)
        self.wallet[cur] += val
        self.money_deals += 1


    def load_from_db(self):
        '''
        Returns wallet.
        '''
        sql_query = "SELECT * FROM money WHERE players_id=%(id)s"
        sql_data = {"id": self.player_id}
        data = self.db.run_query(sql_query, sql_data)
        for w in data:
            self.wallet[w[1]] = w[2]

    def save_to_db(self, id, currency, value):
        '''
        All currencies must have unique id.
        '''
        try:
            sql_query = "INSERT INTO mydb.money (id, currency, value, created, updated, players_id)" \
                        " VALUES (%(id)s, %(currency)s, %(value)s, now(), now(), %(players_id)s);"
            sql_data = {"id": id,
                        "currency": currency,
                        "value": value,
                        "players_id": self.player_id}
            self.db.run_query(sql_query, sql_data)

        except Exception as er:
            print(er)
            sql_query = "UPDATE `money`" \
                        " SET `value`=%(value)s, `updated`=now()" \
                        " WHERE `currency`=%(currency)s AND `players_id`=%(players_id)s;"
            sql_data = {"value": value,
                        "currency": currency,
                        "players_id": self.player_id}
            self.db.run_query(sql_query, sql_data)

    def delete_from_db(self, id):
        sql_query = "DELETE FROM `money`" \
                    " WHERE  id=%(id)s;"
        sql_data = {"id": id}
        self.db.run_query(sql_query, sql_data)
        print('DEBUG: delete_from_db ex')







if __name__ == '__main__':

    m = Money(1)

    m.load_from_db()
    m.show_wallet()

    m.save_to_db(3, 'BLR', 55555555)
    m.save_to_db(6, 'P', 1)
    m.delete_from_db(4)
    m.show_wallet()



