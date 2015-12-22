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

class MoneyOp(object):
    def give_money(self, cur, val):
        if cur == 'USD':
            self.money1 -= val
        if cur == 'RUB':
            self.money2 -= val
    def take_money(self, cur, val):
        if cur == 'USD':
            self.money1 += val
        if cur == 'RUB':
            self.money2 += val




class Player(MoneyOp):

    def __init__(self, plr_name, login, email, password):
        self.name = plr_name
        self.login = login
        self.email = email
        self.password = password

        self.health = 100
        self.experience = 0
        self.attack = 1
        self.speed = 1

        self.money1 = 0     # USD
        self.money2 = 0     # RUB

        self.session = 0






p = Player('name', 'log', 'email', 'pass')
print(p.money1)
p.take_money('USD', 100)
print(p.money1)


