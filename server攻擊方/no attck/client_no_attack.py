#!/usr/bin/env python
# -*-coding:utf-8 -*-
import socket, struct, json
download_dir = r'D:\_icando\iwantto\駭客\駭客組寒訓 2020.02.26\socket_兩方攻擊\server攻擊方\no attck'
gd_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
gd_client.connect(('127.0.0.1',8123))
while True:
  cmd=input('>>: 請輸入:get 檔名-->').strip() #get a.txt
  if not cmd:continue
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
      print('總大小：%s  已下載大小：%s' % (total_size, recv_size))
gd_client.close()