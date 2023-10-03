from Instances import Instances
import inspect
import socket

class Server:

    def __init__(self,host = '0.0.0.0',port = 8080):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.methods = {}

    def register_instance(self, instance):
        for funcName,function in inspect.getmembers(instance, predicate=inspect.ismethod):
            if not funcName.startswith('__') and not funcName.startswith('sup'):
                self.methods.update({funcName: function})

    def run(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind(self.address)
            s.listen(1)

            print(f"servidor {self.address} ativo.")
            clientSocket, clientAddres = s.accept()
            print(f"conexão com:\n{clientSocket}\n{clientAddres}")
            while True:
                try:
                    receive = clientSocket.recv(1024).decode('utf-8')
                    p = receive.split('.') 

                    if p[0] == "function list":
                        keys = list(self.methods.keys())
                        send = ', '.join(keys)
                        clientSocket.sendall(str(send).encode('utf-8'))
                        continue
                    
                    send = self.methods[p[0]](int(p[1])) # melhorar para mais de 1 parâmetro
                                                         # quebra alguns tratamentos de erro.

                except KeyboardInterrupt:
                    print(f"servidor {self.address} interrompido")
                    break
                except IndexError:
                    send = "Parâmetros estão faltando"
                except KeyError:
                    send = "Comando desconhecido"
                except ValueError:
                    send = "Valor inválido para número inteiro"
                except ConnectionAbortedError:
                    print("Uma conexão estabelecida foi anulada pelo software no computador host")
                    s.close()
                    break
                clientSocket.sendall(str(send).encode('utf-8'))
                    
                    
def main():
    server = Server()
    inst = Instances()
    server.register_instance(inst)
    server.run()


if __name__ == "__main__":
    main()