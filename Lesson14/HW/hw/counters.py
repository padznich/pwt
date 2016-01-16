# coding=utf-8

import MySQLdb

class Counters(object):

    def __init__(self, name):
        self.name = name
        self.counter = 0


    def add(self, value):
        self.counter += value

    def rob(self, value):
        self.counter -= value

    def show_score(self):
        print("{}".format(self.counter))
