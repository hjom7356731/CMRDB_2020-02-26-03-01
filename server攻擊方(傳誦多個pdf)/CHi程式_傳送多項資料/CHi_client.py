# 接
import socket, sys, threading

from time import sleep

host, port = '127.0.0.1', 442


class recv_data :
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mysocket.connect((host, port))

    def __init__(self):
        while True:
            data = self.mysocket.recv(1024)
            print("fileName: " + data.decode())
            if data == bytes(''.encode()):
                break
            f = open('data/'+data.decode(), 'wb')
            while data != bytes(''.encode()):
                data = self.mysocket.recv(1024)
                print(data)
                # print("內容：" + data)
                if(data == 'exit'.encode()):
                    break
                f.write(data)

re = recv_data()