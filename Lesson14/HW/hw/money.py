# coding=utf-8

import connectordb

class Money(object):

    def __init__(self, player_id):

        self.player_id = player_id
        self.wallet = {} # {currency : amount}
        self.money_deals = 0

        self.db_connect = connectordb.Connect

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
        data = self.db_connect.load_money_db(self.player_id)
        self.wallet = data

    def save_to_db(self, *args):
        '''
        All currencies must have unique id.
        '''
        try:
            self.db_connect.insert_into_money_table(args[0], args[1], args[2], args[3])
        except Exception as er:
            print(er)
            self.db_connect.update_money_table(args[0], args[1], args[2], args[3])

if __name__ == '__main__':
    m = Money(1)
    m.db_connect = m.db_connect('localhost', 'pad', 'padznich', 'hw14')
    m.save_to_db(3, 'EUR', 77, 1)
    m.db_connect.show_table('money')

    m.load_from_db()
    m.show_wallet()

