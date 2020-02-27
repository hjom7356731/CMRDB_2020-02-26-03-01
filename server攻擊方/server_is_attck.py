#!/usr/bin/env python
# -*-coding:utf-8 -*-
import socket
import subprocess
import struct
import json
import os

share_dir = r'D:\_icando\iwantto\駭客\駭客組寒訓 2020.02.26\socket_兩方攻擊\server攻擊方'

gd_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
gd_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
gd_server.bind(('127.0.0.1', 8123)) # 0-65535: 0-1024給作業系統使用
gd_server.listen(5)

while True:
    print('server已成功開啟，等待client要求檔案中...')
    conn, client_addr = gd_server.accept()
    while True: # 通訊迴圈
        try:
            # 1、收命令
            res = conn.recv(8096) # b'get 1.txt'
            if not res: break # 適用於linux作業系統
            # 2、解析命令，提取相應命令引數
            print('收到client端的檔案請求')
            cmds = res.decode('utf-8').split() # ['get','1.txt']
            filename = cmds[1]
            # 3、以讀的方式開啟檔案,讀取檔案內容傳送給客戶端
            # 第一步：製作固定長度的報頭
            header_dic = {
            'filename': filename, # 1.txt
            'file_size':os.path.getsize(r'%s\%s'%(share_dir, filename)) # 路徑/1.txt
            }
            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')
            # 第二步：先發送報頭的長度
            conn.send(struct.pack('i',len(header_bytes)))
            # 第三步:再發報頭
            conn.send(header_bytes)
            # 第四步：再發送真實的資料
            with open('%s/%s'%(share_dir, filename),'rb') as f:
                for line in f:
                    conn.send(line)
        
        except ConnectionResetError: # 適用於windows作業系統
            break
    conn.close()
gd_server.close()