import socket

socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 999

socketserver.bind((HOST, PORT))

socketserver.listen(5)
print("等待客户端连接……")
clientsocket, addr = socketserver.accept()
print("已建立连接, 开始数据传输……")

while True:

    recvmsg = clientsocket.recv(1024)
    strData = recvmsg.decode("utf-8")
    print(strData)
