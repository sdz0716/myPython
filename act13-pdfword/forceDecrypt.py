#! python3
# forceDecrypt.py - force decrypt pdf by a guess password file

import PyPDF2

passwdFile = open('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\dictionary.txt')
pdfFile = open('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\watermarkedCover.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
for line in passwdFile.readlines():
    # print(passwdFile.readlines())
    if pdfReader.decrypt(line.strip('\n').lower()) == 1 or pdfReader.decrypt(line.replace('\n', '').upper()) == 1:
        print(line)
        exit()