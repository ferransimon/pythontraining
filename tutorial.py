# tutorial.py
# Data structures

# List/tuple and dics

list_ex = ["Pinapple", "pen", "apple"]
tuple_ex = (1,5)
dict_ex = {"key1": 1, "key2": 2}

# List Comprehensions

squares = []
for x in range(10):
	squares.append(x**2)

print(squares)

squares = [x**2 for x in range(10)]

# Functional tools

a = map(lambda x: x*x*x, range(10))
print(a)

zip_list = zip(list_ex, [0,1,2])

print(zip_list)

filtered_list = filter(lambda x: "n" in x, list_ex)

print(filtered_list)

reduced = reduce(lambda x,y: x+y, [1,2,3,4,5])

print(reduced)

# Classes

class Player(object):

	def __init__(self, life, name):
		self.life = life
		self.name = name

	def hit(self, damage):
		self.life -= damage

	def say_hi(self):
		print(self.name)


class Hero(Player):

	def __init__(self, sword):
		super(Hero, self).__init__(10, "TheHero")
		self.sword = sword

	def attack(self, enemy):
		enemy.hit(self.sword.damage)

class Sword(object):

	def __init__(self, damage):
		self.damage = damage

weapon = Sword(5)
hero = Hero(weapon)
enemy = Player(15, "Ruggero")

hero.say_hi()
hero.attack(enemy)

print(enemy.life)


class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go()
b.go()
c.go()
print(D.mro())
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

# a.pause()
# b.pause()
# c.pause()
d.pause()
#e.pause()


###############

class M(object):
	a = 3

class P(M):
	b = 1

print M.a
print P.a

M.a = 4
print P.a

P.a = 5
print M.a


