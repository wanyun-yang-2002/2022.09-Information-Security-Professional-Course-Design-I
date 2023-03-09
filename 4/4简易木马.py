import subprocess
import shlex


# shell = True cmd执行
# stdout 标准输出s
# shlex.split 分隔复杂命令
def cmd(com: str):
    if com == "exit":
        print("已退出！")
        return com
    return subprocess.run(shlex.split(com), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


a = cmd(input(">"))
while a != "exit":
    print(a.stdout.decode('gbk'), "\n命令执行成功!")  # bytes
    a = cmd(input(">"))

# 以命令行的形式，如dir、ls、rm、del等
