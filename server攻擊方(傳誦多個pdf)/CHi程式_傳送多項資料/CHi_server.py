# 傳
import socket, threading, os
from time import sleep


host, port = '127.0.0.1', 442


class transfer :
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __init__(self):
        self.mysocket.bind((host, port))
        print(' Server is ready ..')
        self.mysocket.listen(5)
        conn, addr = self.mysocket.accept()

        file_name = 'files.txt'
        size = os.path.getsize(file_name)
        print(' file size : {}'.format(str(size)))

        send_thread = threading.Thread(target = self.send_file, args=(file_name, size, conn, addr, ))
        send_thread.start()

    def send_file(self, file_name, size, conn, addr):
        file_list = open('files.txt', 'r')
        for i in file_list:
            file_name = i.rstrip('\n')
            with open(file_name, 'rb') as file:
                conn.send(file_name.encode())
                sleep(1)
                while True:
                    data = file.read()
                    print(data)
                    if data == bytes(''.encode()):
                        conn.send('exit'.encode())
                        sleep(1)
                        break
                    conn.send(data)
                    sleep(1)

                print('File sent successfully.')


#Transfer = transfer()