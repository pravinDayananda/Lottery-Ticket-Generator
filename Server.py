


#!/usr/bin/python3
import os
import signal
import socket
import error
import random

host = 'localhost'
port = 1234
maxConnection = 2056


def signalhandler(signalnumber, frame):
    while True:
        try:
            pid, status = os.waitpid(-1, os.WHOHANG)
        except OSError:
            return
        if pid == 0:
            return
def gen(pool, size):
    number = list(range(1, pool))
    tickets = []
    for i in range(size):
        selected = random.choice(number)
        number.remove(selected)
        tickets.append(selected)
    return str(tickets)
def handlerequest(sock):
    request = sock.recv(1024)
    print("from client" + str(data))
    clientstringlist = list(data.spilt())
    numberoftickets = clientstringlist[2]
    tickettype = clientstringlist[1]
    for i in range(int(numberoftickets)):
        if tickettype == "Max":
            data = gen(50, 7)
            sock.sendall(data.encode())
        elif tickettype == "Lot":
            data = gen(45, 6)
            sock.sendall(data.encode())
        elif tickettype == "649":
            data = gen(49, 6)
            sock.sendall(data.encode())
    else:
        sock.close()

def server():
    sock = socket.socket()
    sock.setopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print("Lottery Ticket Generator")
    sock.bind(server_address)
    sock.listen(maxConnection)

    signal.signal(signal.SIGCHLD, signalHandler)

    while True:
        serversock, clientaddress = sock.accept()
        try:
            pid = os.fork()
        except OSError:
            sys.stderr.write("could not create a child process")
            continue

        if pid == 0:
            sock.close()
            handleRequest(sock)
            serversock.close()
            os._exit(0)
        else:
            sock.close()


if __name__ == '__main__':
    Server()
