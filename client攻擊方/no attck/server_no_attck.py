import socket
import sys
from threading import Thread
import socketserver

buffer_size=1024
host = 'localhost'
port = 9001
class ClientThread(Thread):
    def __init__(self,addr,conn):
        Thread.__init__(self)
        self.addr=addr
        self.conn=conn
        print("You get data from "+addr[0]+":"+str(addr[1]))

    def run(self):
        filename='server_get.png'
        #open(路徑+文件名,讀寫模式) 
        #讀寫模式:r只讀,r+讀寫,w新建(會覆蓋原有文件),a追加,b二進製文件.常用模式
        filein=open(filename,"wb")
        while True:
            data=conn.recv(buffer_size)
            if not data:
                # f.close()關閉文件
                filein.close()
                break
            # f.write("hello\n") #如果要寫入字符串以外的數據,先將他轉換為字符串. 
            filein.write(data)

        print('You are get the file...Successfully ! ')
        conn.close()


# python client.py           ip           port         
#        sys.argv[0]      sys.argv[1]   sys.argv[2]   

threads=[]
# 建TCP Socket：
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
while True:
    sock.listen(10)
    print('waiting your client.......ing')
    #  accept接受TCP鏈接並返回（conn, address），clientsock=conn(是一種socket物件)；clientaddr=address(client端的IP)
    conn,addr=sock.accept()
    print('YA!  Get a client! Connected from',addr)

    newthread=ClientThread(addr,conn)
    newthread.start()
    # list.append(obj) 在list[]最後面加入obj(可以是字串、物件...)
    threads.append(newthread)

for t in threads:
    t.join()




