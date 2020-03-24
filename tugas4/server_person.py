from socket import *
import socket
import threading
import logging
import time
import sys

from person_machine import PersonMachine

pm = PersonMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data=b''
            while True:
                isi = self.connection.recv(100)
                if not isi:
                    break
                data+=isi
                
            if data:
                dd=b'null'
                if(len(data.split(b'AOE', 1))==2):
                    dd, data = data.split(b'AOE', 1)
                d = data.decode()
                cstring = d.split(" ")
                command = cstring[0].strip()
                hasil = pm.proses(d, dd)
                if(command == "download"):
                    self.connection.sendall(hasil)
                if (command == "list"):
                    self.connection.sendall(hasil.encode())
                if(command == "upload"):
                    self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('localhost', 8889))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

