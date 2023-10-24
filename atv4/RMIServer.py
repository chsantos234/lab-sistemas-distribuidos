import Pyro5.api
from random import randint

# classe da atividade
@Pyro5.api.expose
class GreetingMaker():
    def get_fortune(self,name):
        value = randint(0,10000)
        return f"Hello, {name}. Here is your fortune message:\nTomorrow's lucky number is {value}."

# classe nova adicionada (duas funções)
@Pyro5.api.expose
class Math():

    def sum(self,valores):
        return sum(valores)
    
    def mult(self,valores):
        multi = 1
        for i in valores:
            multi *= i
        return multi 


daemon = Pyro5.server.Daemon() # Pyro daemon
ns = Pyro5.api.locate_ns() # Pesquisa do servidor

# registro das classes como objetos Pyro
uri = daemon.register(GreetingMaker)
uri2 = daemon.register(Math)

# registro dos objetos com um nome no servidor
ns.register("example.greeting", uri)
ns.register("example.math", uri2)

print("Ready.")

# inicializa o loop de eventos do servidor e espera uma conexão
daemon.requestLoop()