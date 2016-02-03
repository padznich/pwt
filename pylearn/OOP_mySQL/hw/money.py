# coding=utf-8

import connectordb

class Money(object):

    def __init__(self, players_id):

        self.ids = {} # {currency : id}
        self.players_id = players_id
        self.wallet = {} # {currency : amount}
        self.money_deals = 0

        self.db = connectordb.db_connect

    def show_wallet(self):
        print("Player id : {}. Wallet:".format(self.players_id))
        for k, v in self.wallet.items():
            print('-- {} : {}'.format(k, self.wallet[k]))

    def rob(self, cur, value):
        print("Player id: {}. Balance decreased by {} {}.".format(self.players_id, value, cur))
        self.wallet.setdefault(cur, 0)
        self.wallet[cur] -= value
        self.money_deals += 1

    def add(self, cur, value):
        print("Player id: {}. Balance increased by {} {}.".format(self.players_id, value, cur))
        self.wallet.setdefault(cur, 0)
        self.wallet[cur] += value
        self.money_deals += 1



    def load_from_db(self):
        '''
        Reestablish wallet.
        '''
        sql_query = "SELECT * FROM money WHERE players_id=%(players_id)s"
        sql_data = {"players_id": self.players_id}
        data = self.db.run_query(sql_query, sql_data)
        for w in data:
            self.wallet[w[1]] = w[2]
            self.ids[w[1]] = w[0]

    def save_to_db(self):
        '''
        At first update all values. If appears a new currency - it causes an exception.
        And insert a new currency: value.
        '''
        for currency, value in self.wallet:

            try:
                sql_query = "UPDATE money" \
                            " SET value=%(value)s, updated=now()" \
                            " WHERE currency=%(currency)s AND players_id=%(players_id)s;"
                sql_data = {"value": value,
                            "currency": currency,
                            "players_id": self.players_id}
                self.db.run_query(sql_query, sql_data)

            except Exception as er:
                print(er)
                for currency, value in self.wallet:
                    sql_query = "INSERT INTO money (id, currency, value, created, updated, players_id)" \
                                " valueS (%(id)s, %(currency)s, %(value)s, now(), now(), %(players_id)s);"
                    sql_data = {"id": self.ids[currency],
                                "currency": currency,
                                "value": value,
                                "players_id": self.players_id}
                    self.db.run_query(sql_query, sql_data)

    def delete_from_db(self, id):
        '''
        Delete from money by id.
        '''
        sql_query = "DELETE FROM `money`" \
                    " WHERE  id=%(id)s;"
        sql_data = {"id": id}
        self.db.run_query(sql_query, sql_data)


if __name__ == '__main__':

    m = Money(1)

    m.load_from_db()
    m.show_wallet()

    #m.delete_from_db(3)



