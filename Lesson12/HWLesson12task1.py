# coding=utf-8

from time import sleep

from gm import person

# while 1:
#     sleep(1000)
#     reload(person)



p1 = person.Player('Bob', 'akhalai', 'bob@mail.ru', 'pass1')
p2 = person.Moderator()
p3 = person.Admin()



print(p1.name)
p1.session.__enter__()
p1.money.take('RUB', 500)
p1.money.show_wallet()
p1.money.give('RUB', 200)
p1.money.take('USD', 900)
p1.money.show_wallet()
sleep(0.4)
p1.session.__exit__()
sleep(0.2)
p1.session.__enter__()
sleep(0.1)
p1.session.__exit__()
p1.session.show_info()

p1.say()
p2.say()
p3.say()