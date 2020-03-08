import sys
import socket
import threading

ports = [31000, 31001, 31002]

def do_thread(i):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', i)
    print(f"starting up on {server_address}")

    sock.bind(server_address)
    sock.listen(1)

    print("waiting for a connection")
    connection, client_address = sock.accept()
    
    print(f"Handle connection from {client_address}")
    while True:
        data = connection.recv(32)
        print(f"[ Port {i}] received {data}")
        if data:
            print(f"[ Port {i}] sending back data")
            connection.sendall(data)
        break
        
    connection.close()

# Listen for incoming connections
multi_threads = []
for i in ports:    
    thr = threading.Thread(target=do_thread, args=(i,))
    multi_threads.append(thr)

for thr in multi_threads:
    thr.start()

print('Exit')