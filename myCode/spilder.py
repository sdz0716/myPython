#！ python3
# 该脚本包括ssh连接后执行命令，ssh隧道连接后使用mysql，urllib用于web下载且使用cookie登录
# datatime获取当前时间，smtplib用于发送邮件，email.mime用于构建邮件，可生成html格式的内嵌图片的有邮件


import re
import os
import urllib.request, urllib.parse
import http.cookiejar
import datetime
import mysql.connector
# import paramiko
import sshtunnel
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.10.61', 22, 'root', 'fairlink')
# stdin,stdout,stderr = ssh.exec_command('free -m')
# print(stdout.read())

with sshtunnel.SSHTunnelForwarder(
        ('xx.xx.xx.xx', 22),
        ssh_password='password',
        ssh_username='account',
        remote_bind_address=('127.0.0.1', 3306)
) as server:
    cnn = mysql.connector.connect(host='127.0.0.1', user='account', password='password', port=server.local_bind_port, database='databasename')
    cursor = cnn.cursor()
    cursor.execute("select graphid from graphs_items where graphs_items.itemid=(select itemid from items join hosts on hosts.hostid=items.hostid where hosts.host='xx.xx.xx.xx' and items.name='Available memory')")
    results = cursor.fetchone()
    print(results[0])
    cursor.close()
    cnn.close()

url = 'url'
value = {'name': 'loginAccount', 'password': 'password', 'autologin': '1', 'enter': 'Sign in', 'request': ''}
data = urllib.parse.urlencode(value).encode('utf-8')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0')]
req = opener.open(url, data)
req = opener.open('http://xx.xx.xx.xx/zabbix/chart2.php?graphid=%d&period=86400&width=800&stime=20161129000000' % results[0])
# print(req.geturl())
# print(req.read())
file = open('C:\\Users\\path\\path\\1.png', 'wb')
file.write(req.read())
file.close()

msg = MIMEMultipart('related')
msg['Subject'] = 'Zabbix'
msg['From'] = 'account@x.com'
msg['To'] = 'account@x.com'
message = '''
<p>test graph</p>
<p><img src="cid:image1"></p>
'''
message = MIMEText(message, 'html')
msg.attach(message)
file = open('C:\\Users\\path\\path\\1.png', 'rb')
# print(file.read())
msgImage = MIMEImage(file.read())
file.close()
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
# smtp.connect('smtp.exmail.qq.com')
smtp.login('account@x.com', 'password')
smtp.sendmail(msg['From'], msg['To'], msg.as_string())
smtp.quit()

