from Instances import Instances
import inspect
import socket

class Server:

    def __init__(self,host = '0.0.0.0',port = 8080):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.methods = {}

    #def register_method(self, function):
    #    self.method.update({function.__name__:function})

    def register_instance(self, instance):
        for funcName,function in inspect.getmembers(instance, predicate=inspect.ismethod):
            if not funcName.startswith('__'):
                self.methods.update({funcName: function})

    def run(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind(self.address)
            s.listen(1)

            print(f"servidor {self.address} ativo.")

            while True:
                try:
                    clientSocket, clientAddres = s.accept()
                    print(f"conexão com:\n{clientSocket}\n{clientAddres}")

                    receive = clientSocket.recv(1024).decode('utf-8')
                    p = receive.split(';')
                    send = self.methods[p[0]](int(p[1]),int(p[2])) # erro
                    clientSocket.sendall(str(send).encode('utf-8'))

                except KeyboardInterrupt:
                    print(f"servidor {self.address} interrompido")
                    break
                #except Exception as e:
                #    print(f"Erro: {e}")
                #    break
                #finally:
                #    s.close()
                    
                    
def main():
    server = Server()
    inst = Instances()
    server.register_instance(inst)
    server.run()


if __name__ == "__main__":
    main()