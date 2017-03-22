#! python3
# 随机将工作通过邮件发送给随机账户

import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header

work = ['aaa', 'bbb', 'ccc']
email = 'account@fairlinkcentury.com'

smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
smtpObj.login('account@fairlinkcentury.com', 'password')

while work != []:
    chores = random.choice(work)        #列表中随机选择
    body = "sdfasdfasdfasdfasfadsfwork is %s" % chores
    message = MIMEText(body)
    message['From'] = Header('SS')
    message['To'] = Header('DDZZ')
    subject = 'ceshi'
    message['Subject'] = Header(subject)
    smtpObj.sendmail('account@fairlinkcentury.com', 'account@fairlinkcentury.com', message.as_string())
    work.remove(chores)     #删除列表中值
smtpObj.quit()