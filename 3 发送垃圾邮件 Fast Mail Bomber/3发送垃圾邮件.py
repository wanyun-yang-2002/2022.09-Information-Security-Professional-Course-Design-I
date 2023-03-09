from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import time


def sendMail(message, Subject, sender_show, recipient_show, to_addrs, cc_show=''):
    # 填写真实的发邮件服务用户名
    user = '2354839133@qq.com'
    password = 'cdrrbztqusvuebjh'
    # 邮件内容
    msg = MIMEText(message, 'plain', _charset="utf_8")
    # 邮件主题描述
    msg["Subject"] = Subject
    # 发件人显示，不起实际作用
    msg["from"] = sender_show
    # 收件人显示，不起实际作用
    msg["to"] = recipient_show
    # 抄送人显示，不起实际作用
    msg["Cc"] = cc_show
    with SMTP_SSL(host="smtp.qq.com", port=465) as smtp:
        # 登陆发邮件服务器
        smtp.login(user=user, password=password)
        # 实际发送，接收邮件配置
        smtp.sendmail(from_addr=user, to_addrs=to_addrs.split(','), msg=msg.as_string())


if __name__ == '__main__':
    message = input("输入邮件正文：")     # 邮件正文
    Subject = input("输入邮件主题：")     # 邮件主题
    # 发件人名字
    sender_show = input("输入发件人名字：")
    # 接收人名字
    recipient_show = input("输入收件人名字：")
    # 实际发给的接收人
    email_list = []
    cs = int(input("输入发送次数："))
    sleeptime = int(input("输入邮件发送时间间隔(秒)："))
    b = 1
    while b == 1:
        a = input("输入收件人邮箱：")
        email_list.append(a)
        b = int(input("继续请按1，退出请按0:"))
        if b == 0:
            continue
    for i in email_list:
        to_addrs = i
        for a in range(1, cs + 1):
            time.sleep(sleeptime)
            sendMail(message, Subject, sender_show, recipient_show, to_addrs)
    print("批量发送完成")
