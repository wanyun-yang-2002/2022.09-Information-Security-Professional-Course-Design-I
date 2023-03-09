print("-------------------服务端------------------------")
import socket

# import time
HOST = ""  # HOST变量是空白 表示它可以使用任何可用地址
PORT = 999  # 端口号
ADDR = (HOST, PORT)  # （HOST， ）原组限制传值的数量

tcpSerSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# tcpCliSock = socket.socket()
tcpSerSock.bind(ADDR)  # 建立连接
tcpSerSock.listen(5)  # 开始Tcp监听， 最多监听5个请求

while True:
    print("等待客户连接")
    tcpCliSock, addr = tcpSerSock.accept()  # 阻塞方法
    print(f"收到来自\t{addr}\t的连接")
    while True:
        print("等待消息:")
        data = tcpCliSock.recv(1024)  # 每次接受1024M的信息
        print(f"收到信息：{data.decode('utf-8')}")
        # tcpClisock.send(bytes("[{}]:{}".format(time.time(),data), "utf-8")
        # tcpClisock.send(b"收到消息啦！")#也可以用下面的方法实现
        tcpCliSock.send("收到消息啦！".encode('utf-8'))  # 发bytes数组
    tcpCliSock.close()
