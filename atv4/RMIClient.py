import Pyro5.api

name = input("What is your name? ").strip()

greeting_maker = Pyro5.api.Proxy("PYRONAME:example.greeting") # use name server object lookup uri shortcut
math_maker = Pyro5.api.Proxy("PYRONAME:example.math")

print(greeting_maker.get_fortune(name))
print(math_maker.sum(1,2,3,4,5))
print(math_maker.mult(1,2,3,4,5))