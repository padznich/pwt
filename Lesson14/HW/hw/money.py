# coding=utf-8

import connectordb

class Money(object):

    def __init__(self, name):
        self.wallet = {} # {currency : amount}
        self.name = name
        self.money_deals = 0

        self.connect = connectordb.Connect

    def show_wallet(self):
        print("{}'s wallet:".format(self.name))
        for k, v in self.wallet.items():
            print('--{} : {}'.format(k, self.wallet[k]))

    def give(self, cur, val):
        print("{} balance decreased by {} {}.".format(self.name, val, cur))
        self.wallet.setdefault(cur, 0)
        self.wallet[cur] -= val
        self.money_deals += 1

    def take(self, cur, val):
        print("{} balance increased by {} {}.".format(self.name, val, cur))
        self.wallet.setdefault(cur, 0)
        self.wallet[cur] += val
        self.money_deals += 1



    def save_to_db(self, *args):

        try:
            self.connect.insert_into_money_table(args[0], args[1], args[2], args[3])
        except Exception as er:
            print(er)
            self.connect.update_money_table(args[0], args[1], args[2])

if __name__ == '__main__':
    m = Money('test_money')
    m.connect = m.connect('localhost', 'pad', 'padznich', 'hw14')
    m.save_to_db(44, 'GBH', 1)
    m.connect.show_table('money')

