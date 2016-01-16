
import person

p = person.Admin()
p.say()

p.db_connect = p.db_connect('localhost', 'pad', 'padznich', 'hw14')

p.load_player(1)

print(p.id)
