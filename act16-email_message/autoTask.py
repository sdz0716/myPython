#! python3
# 通过邮件获得执行命令，执行任务

import subprocess
import imapclient
import pyzmail
import pprint
import re

cmdRe = re.compile(r'\'(.*)\'')     #不能带单引号，否则无法执行

imapObj = imapclient.IMAPClient('pop.exmail.qq.com', ssl=True)
imapObj.login('account@fairlinkcentury.com', 'password')

# pprint.pprint(imapObj.list_folders())

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ALL'])      #疑似邮箱问题，通过标题等搜索报错
# print(UIDs)
rawMessage = imapObj.fetch(33882, ['BODY[]'])
# pprint.pprint(rawMessage)

message = pyzmail.PyzMessage.factory(rawMessage[33882][b'BODY[]'])      #需要使用二进制表示
# print(message.get_addresses('subject'))

text = message.text_part.get_payload().decode(message.text_part.charset)
# print(text)
cmd = cmdRe.findall(text)
print(cmd[0])
mm = 'C:\\Windows\\System32\\calc.exe'
print(mm)
subprocess.Popen(cmd[0])