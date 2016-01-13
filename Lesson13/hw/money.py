# coding=utf-8


class Money(object):

    def __init__(self, name):
        self.wallet = {} # {currency : amount}
        self.name = name
        self.money_deals = 0

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