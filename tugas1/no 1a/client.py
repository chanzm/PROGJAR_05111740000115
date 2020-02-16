import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

data_kirim = open("kirim.txt","rb")
try:
    while True:
        mtr = data_kirim.read(256)
        if not mtr:
            break
        sock.send(mtr)

    print("file terkirim")
    
    data_kirim.close()

finally:
    sock.close()