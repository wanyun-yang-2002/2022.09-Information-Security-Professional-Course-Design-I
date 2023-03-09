print("-------------------客户端------------------------")
import socket
HOST = "localhost"
POST = 999
ADDR = (HOST, POST)

#tcpCliSock = socket.socket()
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)#客户端主动建立连接

while True:
    data = input("> ")
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(1024)#一般信息不会很大可以一次性接收完（1024可以不写）
    if not data:
        break
        print(data.decode('utf-8'))
tcpCliSock.close()