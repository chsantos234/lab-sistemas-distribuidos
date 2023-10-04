import socket

class Client:
    def __init__(self,host = 'localhost',port = 8080):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.sock = None

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.settimeout(5.0)
            self.sock.connect(self.address)
        except Exception as e:
            print(e)

    def disconnect(self):
        try:
            self.sock.close()
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

            client.sock.sendall(bytes(send,'utf-8'))
            receive = client.sock.recv(1024)

            print(receive.decode('utf-8'),"\n")
        except TimeoutError as e:
            print(e)
        except KeyboardInterrupt:
            print(f"cliente {client.address} interrompido")
            client.disconnect()
            break

if __name__ == "__main__":
    main()