from Instances import Instances
import inspect
import socket

class Server:

    def __init__(self,host = '0.0.0.0',port = 8080):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.methods = {}
        self.desc = '''Comandos do servidor:\n\nhelp: descrição das utilidades do servidor.\nf-list: lista de funções.\ndesc,função: descrição de uma função.\nfunção,params: executa função.'''

    def register_instance(self, instance):
        for funcName,function in inspect.getmembers(instance, predicate=inspect.ismethod):
            if not funcName.startswith('__') and not funcName.startswith('sup'):
                self.methods.update({funcName: function})

    def response_handler(self,resp):
        send = ''
        
        # para o retorno de informações das funções
        if resp[0] == "f-list":
            send = ', '.join(list(self.methods.keys()))
        elif resp[0] == "desc":
            method = self.methods[resp[1]]
            send = method.__doc__
        elif resp[0] == 'help':
            send = self.desc
        else:
            # para a utilização das funções
            send = self.methods[resp[0]](*resp[1:])
        return send


    def run(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind(self.address)
            s.listen(1)

            print(f"servidor {self.address} ativo.")
            clientSocket, clientAddres = s.accept()
            print(f"conexão com: {clientAddres}")

            while True:
                try:
                    resp = clientSocket.recv(1024).decode('utf-8').split(',')
                    send = self.response_handler(resp)

                # tratamentos de erros com envio de mensagens personalizadas
                except IndexError:
                    send = "Parâmetros estão faltando"
                except KeyError:
                    send = "Comando desconhecido"
                except (ValueError,TypeError):
                    send = "Parâmetros de entrada inválidos ou incompletos"
                except (ConnectionAbortedError,KeyboardInterrupt):
                    print(f"servidor {self.address} interrompido")
                    s.close()
                    break

                # envio da resposta para o socket cliente
                clientSocket.sendall(str(send).encode('utf-8'))
                    
                    
def main():
    server = Server()
    inst = Instances()
    server.register_instance(inst)
    server.run()


if __name__ == "__main__":
    main()