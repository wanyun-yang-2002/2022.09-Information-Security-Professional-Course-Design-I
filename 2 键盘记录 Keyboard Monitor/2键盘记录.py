# 监控键盘
from pynput import keyboard
import time

def on_press(key):      # 按下键盘捕捉key
    print(f'{key}:pushed')
    print(time.asctime())   # 将收到的结果进行有效的实时显示

def on_release(key):    # 松开按键捕捉key
    # print(f'{key} released')
    if key == keyboard.Key.esc:     # 码
        # stop listener
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as lsn:
    lsn.join()      # 使用多线程的方法去监听
