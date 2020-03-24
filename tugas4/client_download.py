import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8889

# Connect the socket to the port where the server is listening
server_address = ('localhost', port)
print(f"connecting to {server_address} port {port}")
sock.connect(server_address)

Filename = input("nama file : ")

Data="download "+Filename
sock.send(Data.encode('utf-8'))
sock.shutdown(socket.SHUT_WR)

data = sock.recv(1024)
if data == b'File not Exist':
    print("File gaada")
else:
    f = open("File Client/"+Filename, 'wb')  # open in binary
    while (data):
        f.write(data)
        data = sock.recv(1024)
    print("File Terdownload")
    f.close()

print("closing")
sock.close()