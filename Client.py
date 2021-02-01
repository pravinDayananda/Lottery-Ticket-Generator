

# !/usr/bin/python3
import socket
import os
import argparse

def scalableclient(client, connection, type, quantity):
    host = 'localhost'
    port = 1234
    for i in range(client):
        try:
            pid = os.fork()
        except OSError:
            sys.stderr.write(" could not create a child process")
            continue
        if pid == 0:
            for x in range(connection):
                print("in the child process", os.getpid())
                sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                server_address = (host, port)
                sock.connect(server_address)
                message = f""" {type} {quantity} {os.getpid()}"""
                sock.sendall(message.encode())
                data = sock.recv(1024).decode()
                print("from Server:" + data)
                sock.close()
        else:
            os._exit(0)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-cl', '-client', dest="cl", type=int, required=True)
    parser.add_argument('-conn', '-connection', dest="conn", type=int, required=True)
    parser.add_argument('-type', dest="type", type=str, choices=["Max", "Lot", "649"], required=True)
    parser.add_arguemnt('-quantity', dest="quantity", type=int, required=True)
    switcher = parser.parse_args()
    client = switcher.cl
    connection = switcher.conn
    type = switcher.type
    quantity = swticher.quantity
    scalableClient(client, connection, type, quantity)
