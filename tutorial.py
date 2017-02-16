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
# with list comprehension
a = [x*x*x for x in range(10)]
print(a)

zip_list = zip(list_ex, range(3))
print(zip_list)

filtered_list = filter(lambda x: "n" in x, list_ex)
print(filtered_list)
#with list comprehension
filtered_list = [x for x in list_ex if "n" in x]
print(filtered_list)

reduced = reduce(lambda x,y: x+y, [1,2,3,4,5])
print(reduced)

print("Is there any pen in list: " + str(any([x for x in list_ex if "pen" == x])))
print("All elements are pen: " + str(all(["pen" == x for x in list_ex])))

# args and kwargs

def test(*args, **kwargs):
    print(args)
    print(kwargs)


test("I am an arg", keyword="I am a kwarg")

params = ("I am an arg", )

kparams = {
    "keyword" : "I am a kwarg"
}

test(*params, **kparams)

#Default params

def test2(num, mem=[]):
    [mem.append(x) for x in range(num)]
    print mem

test2(3)
test2(3, [])
test2(3)

def test3(num, mem=None):
    if not mem:
        mem = []
    [mem.append(x) for x in range(num)]
    print mem

test3(3)
test3(3, [])
test3(3)


def fib(n, mem={}):
    if n <= 2:
        return 1
    else:
        val = mem.get(str(n-1), fib(n-1)) + mem.get(str(n-2), fib(n-2))
        mem[str(n)] = val
        return val

print(fib(20))

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

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()


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


