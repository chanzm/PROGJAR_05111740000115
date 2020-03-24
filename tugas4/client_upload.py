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
if os.path.isfile("File Client/" + Filename):
    fixing = "upload " + Filename
    print("Mengirim: " + Filename)
    myfile = open("File Client/" + Filename, "rb")
    Filename = "AOE" + fixing
    e = Filename.encode("utf-8")
    datasend = myfile.read() + e
    sock.send(datasend)
    sock.shutdown(socket.SHUT_WR)
    hasil = sock.recv(10).decode()
    print(hasil)
else:
    print("File gaada")

print("Closing")
sock.close()