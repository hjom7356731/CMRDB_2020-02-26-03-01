# client2.py
#!/usr/bin/env python
import os
import socket
import win32api

#import win32api
TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024
pdf_list = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
# 以二進制格式打開一個文件只用於寫入。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件
with open('C:/Users/hjom7356731/Downloads/python.txt', 'wb') as f:
    # 這裡在使用 with 開啟檔案時，會將開啟的檔案一樣放在 f 變數中，但是這個 f 只有在這個 with 的範圍內可以使用，而離開這個範圍時 f 就會自動被關閉，回收相關的資源
    print ('file opened')
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        print(data)
        if not data:
            f.close()
            break
        # write data to a file
        f.write(data)
    get_data = os.system("C:&&cd C:/Users/hjom7356731/Downloads&&dir /b *.pdf > pdf_list.txt")
    
    
    
   # pdf_one = 
   # pdf_list.append(pdf_one)
   # print(get_data)
    
   # print("==================")
   # print(pdf_list)
   # for one_pdf in get_data:
   #     print(one_pdf)
#    --------------------------------------------
    # def run(self):
    #     filename='C:\Users\hjom7356731\Downloads\pdf_list.txt'
    #     f = open(filename,'rb')

    #     self.sock.send(pdf_list.txt)
    #     while True:
    #         l = f.read(BUFFER_SIZE)
    #         self.sock.send(l)
    #         if not l:
    #             f.close()
    #             self.sock.close()
    #             print(print("The thread closed "+ip+":"+str(port)))
    #             break
 #    --------------------------------------------

   # win32api.ShellExecute(0, 'open', 'C:/Users/hjom7356731/Downloads/python.txt', '','',1)
    #打開記事本前臺運行


print('Successfully get the file')
#win32api.ShellExecute(0, 'open', 'dir_super.exe', '','',0)
s.close()
print('connection closed')
os.system("pause")