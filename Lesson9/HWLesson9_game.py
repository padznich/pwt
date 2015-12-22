# coding=utf-8

'''
Домашнее задание
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
'''

#   ach achievements
#   m1  money1
#   m2  money2
#   gs  game session
class Counter(object): pass

class Player(Counter):

    def __init__(self, plr_name, login, email, password):
        self.name = plr_name
        self.login = login
        self.email = email
        self.password = password

        self.ach1 = 0       # Health
        self.ach2 = 0       # Distance
        self.ach3 = 0       #
        self.ach4 = 0       # health

        self.money1 = 0     # usd
        self.money2 = 0     # rub

        self.session = 0

class Money_op:
    def pop_money(self, cur, val):
        if cur == 'USD':
            self.money1 -= val
        if cur == 'RUB':
            self.money2 -= val

    def add_money(self, cur, val):
        if cur == 'USD':
            self.money1 += val
        if cur == 'RUB':
            self.money2 += val





p = Player('name', 'log', 'email', 'pass')


