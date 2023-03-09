# 服务端,监听，发送命令，等待结果
from socket import socket

print("等待连接...")
serv = socket()
serv.bind(('localhost', 9999))
serv.listen(5)
tcp, _ = serv.accept()  # 放在循环外面可实现客户端执行命令并发挥结果后不自动退出
print('已连接！')
print("输入“exit”退出连接")
while True:
    cmd = input('> ')
    tcp.send(cmd.encode('utf-8'))   # 下达命令
    if cmd == "exit":
        print("断开连接")
        break
    data = tcp.recv(1024)   # 接收客户端的命令执行结果
    print(data.decode('gbk'))   # data是字节数组
serv.close()
print("已退出！")
