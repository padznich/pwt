# coding=utf-8

'''
Домашнее задание 9
Объекты реального мира:
    игрок,
    игровая сессия,
    деньги игрока,
    достижения игрока,
    счетчики игрока.
Некоторые факты:
1. игрок заходит в игру, используя логин(email) и пароль
2. игрок хочет иметь уникальное имя в игре
3. время между моментом ухода и прихода игрока считается
4. игрок может иметь одну или более виртуальных игровых валют(деньги игрока),
    которые используются для совершения игровых действий
5. при прохождение игры игрок получает различные игровые достижения
6. с каждым игроком ассоциировано некоторое количество счетчиков, которые описывают прогресс игрока в игре
7. некоторые счетчики игрока используются для выдачи игровых достижений

Домашнее задание + задача на занятия одновременно 10
Реализовать в Python­коде модель предметной области из предыдущего домашнего
задания. Добавить в модель несколько разновидностей игроков: обычный игрок,
модератор игры, администратор игры. Игроки типа модератор и администратор будут
иметь в будущем дополнительные игровые возможности.
Игроков различных типов следует представить в виде иерархии родственных классов.
Также следует продумать возможное поведение таких игроков и реализовать 1­2
полиморфных демо­метода.
Логику работы предметной области реализовать минимально возможную, везде, где это
возможно, следует обойтись вызовом функции print в сочетании с понятной текстовой
строкой.

Задачи для решения на занятии и дома 11
1. Завершить перенос модели предметной области в код
2. Написать несколько простых тестов для реализации модели предметной области:
тесты ­ это простой код, который создает некоторые объекты класса в нужной
последовательности.
3. Добавить в классы предметной области методы save и load, которые будут
записывать объект в файл и восстанавливать объект в памяти из заданного
файла. Выбрать один из методов сериализации для всех объектов иерархии:
pickle или  json.
'''

import datetime
import json

class Money(object):

    def show_money(self):
        print('Your money:')
        for k, v in self.wallet.items():
            print('{} : {}'.format(k, self.wallet[k]))

    def give_money(self, cur, val):
        self.wallet.setdefault(cur, 0)
        self.wallet[cur] -= val

    def take_money(self, cur, val):
        self.wallet.setdefault(cur, 0)
        self.wallet[cur] += val

class Session(object):

    def __enter__(self):
        self.start = datetime.datetime.now()
        self.last_session += 1

    def __exit__(self):
        self.finish = datetime.datetime.now()
        total = (self.finish - self.start)
        self.session[self.last_session] = (self.start, self.finish, total)

class Player(object):

    def __init__(self, plr_name, login, email, password):
        self.name = plr_name
        self.login = login
        self.email = email
        self.password = password

        self.wallet = {} # {currency : amount}
        self.money = Money()

        self.session = {} # {number_of_session : start finish total}
        self.session = Session()
        self.last_session = 0


    def say(self):
        print("I'm a simple Player.")

    def run(self):
        print("My speed is 7 kilometers per hour")


    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "name": self.name
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.name = object_as_dict["name"]
        return object_as_dict

    def __str__(self):
        return '{}(name="{}")'.format(self.__class__.__name__, self.name)

class Moderator(Player):

    def __init__(self, plr_name='Moderator', login='log', email='email', password='pass'):
        Player.__init__(self, plr_name, login, email, password)

    def say(self):
        print("I'm a moderator.")

    def run(self):
        print("My speed is 10 kilometers per hour")

class Admin(Moderator):

    def __init__(self, plr_name='Admin', login='log', email='email', password='pass'):
        Player.__init__(self, plr_name, login, email, password)

    def say(self):
        print("I'm a administrator.")

    def run(self):
        print("My speed is 50 kilometers per hour")



if __name__ == '__main__':

    p1 = Player('Bob', 'akhalai', 'bob@mail.ru', 'pass1')
    p2 = Moderator('John')
    p3 = Admin('Suzi')

    p1.save(open("Bob.txt", "w"))
    print("p1 is {}".format(p1))

    deserialized_p1 = p1
    deserialized_p1.load(open("Bob.txt"))
    print("deserialized player is {}".format(deserialized_p1))


    p2.save(open("Mod.txt", "w"))
    print("p2 is {}".format(p2))

    deserialized_p2 = p2
    deserialized_p2.load(open("Mod.txt"))
    print("deserialized player is {}".format(deserialized_p2))

    p3.save(open("Adm.txt", "w"))
    print("p3 is {}".format(p3))

    deserialized_p3 = p3
    deserialized_p3.load(open("Adm.txt"))
    print("deserialized player is {}".format(deserialized_p3))