import Pyro5.api

@Pyro5.api.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
                "Tomorrow's lucky number is 12345678.".format(name)

@Pyro5.api.expose
class SpringBoot(object):

    def sum(self,*valores):
        soma = 0
        return sum(valores)
    
    def mult(self,*valores):
        multi = 1
        for i in valores:
            multi *= i
        return multi 


daemon = Pyro5.server.Daemon() # make a Pyro daemon
ns = Pyro5.api.locate_ns() # find the name server
uri = daemon.register(GreetingMaker) # register the greeting maker as a Pyro object
uri2 = daemon.register(SpringBoot)
ns.register("example.greeting", uri) # register the obj with a name in the name server
ns.register("example.math", uri2)

print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for calls