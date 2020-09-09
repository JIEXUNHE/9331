import socket
import threading


def deal_client(newSocket: socket.socket, addr):
    while True:
        data = newSocket.recv(1024)
        if data:
            print("%s %s" % (str(addr), data))
        else:
            print("client [%s] quit" % str(addr))
            newSocket.close()
            break


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 8080))
    server.listen(10)
    print("server is running!")
    while True:
        newSocket, addr = server.accept()
        print("client [%s] is connected!" % str(addr))
        client = threading.Thread(target=deal_client, args=(newSocket, addr))
        client.start()


if __name__ == '__main__':
    main()