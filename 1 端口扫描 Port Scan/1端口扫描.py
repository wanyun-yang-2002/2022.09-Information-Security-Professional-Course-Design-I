import sys
import socket
from queue import Queue
from threading import Thread, Lock

jobs = Queue()
lock = Lock()

'''
解析ip范围 端口扫描 判断端口号是否合理 
'''

r = sys.argv  # 返回的是列表
THNUM = 0  # 默认10线程
IPRANGE = []
PORTRANGE = []
IP = ""


def get_ip():
    ip_param = r[1]
    if ip_param.find('-') != -1:

        x = r[1].split('-')[0].split('.')[0]
        y = r[1].split('-')[0].split('.')[1]
        z = r[1].split('-')[0].split('.')[2]
        t = x + '.' + y + '.' + z + '.'

        ip_start = int(r[1].split('-')[0].split('.')[3])
        ip_end = int(float(r[1].split('-')[1]))
        for ip in range(ip_start, ip_end + 1):  # 加1是因为左闭右开的区间
            ip_now = t + str(ip)
            IPRANGE.append(ip_now)
    else:
        global IP
        IP = ip_param
        IPRANGE.append(ip_param)


# 解析线程数
def get_thnum():
    global THNUM
    THNUM = int(r[3])


# 解析端口范围
def get_port():
    port_start = int(r[2].split("-")[0])
    port_end = int(r[2].split("-")[1])
    if port_start > 65535 or port_end > 65535:  # 判断端口范围是否合理
        print('输入端口范围不合理')
    elif port_start <= 0 or port_end <= 0:
        print('输入端口范围不合理')
    else:
        for port in range(port_start, port_end + 1):  # 加1是因为左闭右开的区间
            PORTRANGE.append(port)


# 检测端口是否开放
def scan(address: tuple) -> bool:  # 传值为元组型（地址，端口号） 结果是 True 或者 False
    SC = socket.socket()
    SC.settimeout(1)  # 等待()秒出结果 ()里是秒数

    if SC.connect_ex(address) == 0:
        return True
    else:
        return False


class Product(Thread):
    def run(self) -> None:
        global IP
        for IP in IPRANGE:
            for port in PORTRANGE:
                jobs.put((IP, port))  # 元组 （IP，port）


class Customer(Thread):
    def run(self) -> None:
        while True:
            address = jobs.get()
            if scan(address):
                lock.acquire()
                print(f"【*】{address[0]}\t{address[1]}\tOPEN")
                lock.release()
            jobs.task_done()


def main():
    p = Product()
    p.daemon = True
    p.start()
    for _ in range(THNUM):
        c = Customer()
        c.daemon = True
        c.start()
    jobs.join()


# ip:port ->(元组)
# 400个(IP，port)
if __name__ == "__main__":
    get_ip()
    get_port()
    get_thnum()
    main()
