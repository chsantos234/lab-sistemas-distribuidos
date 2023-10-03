import socket

class Client:
    def __init__(self,host = 'localhost',port = 8080):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.clientSocket = None

    def connect(self):
        try:
            self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.clientSocket.settimeout(5.0)
            self.clientSocket.connect(self.address)
        except Exception as e:
            print(e)

    def disconnect(self):
        try:
            self.clientSocket.close()
        except Exception as e:
            print(e)

def main():
    client = Client()
    client.connect()

    while True:
        try:
            send = input('input: ')

            if send == 'exit': 
                client.disconnect()
                break

            client.clientSocket.sendall(bytes(send,'utf-8'))
            receive = client.clientSocket.recv(1024)

            print(receive.decode('utf-8'))
        except TimeoutError as e:
            print(e)
        except KeyboardInterrupt:
            print(f"cliente {client.address} interrompido")
            client.disconnect()
            break

if __name__ == "__main__":
    main()