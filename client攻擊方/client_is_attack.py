import socket
import sys
host = 'localhost'
port = 9001
buffer_size=1024
filename = "client攻.png"
# 檢查是否有足夠的參數(client.py ip port filename.txt共4個參數)

# python client.py           ip           port         filename.txt
#        sys.argv[0]      sys.argv[1]   sys.argv[2]   sys.argv[3]



# rU或Ua以讀方式打開,同時提供通用換行符支持(PEP 278) 
# w以寫方式打開，
# a以追加模式打開(從EOF開始,必要時創建新文件) 
# r+以讀寫模式打開
# w+以讀寫模式打開(參見w ) 
# a+以讀寫模式打開(參見a ) 
# rb以二進制讀模式打開
# wb以二進制寫模式打開(參見w ) 
# ab以二進制追加模式打開(參見a ) 
# rb+以二進制讀寫模式打開(參見r+ ) 
# wb+以二進制讀寫模式打開(參見w+ ) 
# ab+以二進制讀寫模式打開(參見a+ )

send_file=open(filename,"rb")

# 建TCP Socket：
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#  client端需要的socket函數_connect
# s.connect(address)  其中address是tupple ( sys.argv[1],int(sys.argv[2]) )
# 鏈接到address處的套接字，一般address的格式為tuple(host, port)，如果鏈接出错，則返回socket.error錯誤
sock.connect((host,port))


while True:
    # f.read([size]) size未指定則返回整個文件,如果文件大小>2倍內存則有問題.f.read()讀到文件尾時返回""(空字串) 
    t=send_file.read(buffer_size)
    while(t):
        sock.send(t)
        t=send_file.read(buffer_size)
    if not t:
        # f.close()關閉文件
        send_file.close()
        break

print('You send data ...Successfully !!')
sock.close()

    
