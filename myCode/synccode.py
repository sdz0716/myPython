#! python3

import os
import zipfile
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib

date = datetime.datetime.now().strftime('%m%d')

def zipFolder(path='C:\\Users\\daize\\Desktop\\pythontest\\code'):
    newZip = zipfile.ZipFile('')