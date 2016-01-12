# coding=utf-8

class Session(object):

    def __init__(self, name):
        self.session_info = [] # [[start, finish, total], [],]
        self.name = name

    def __enter__(self):
        self.start = datetime.datetime.now()

    def __exit__(self):
        self.finish = datetime.datetime.now()
        self.total = (self.finish - self.start)
        self.session_info.append("Session started at: {}  ||  "
                                 "Session finished at: {}  ||  "
                                 "Session duration is: {}"
                                 .format(str(self.start), str(self.finish), str(self.total)))

    def show_info(self):
        for w in self.session_info:
            print("{} {}".format(self.name, w))