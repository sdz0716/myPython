#! python3
# finalPdf.py - 遍历目录下所有pdf文件，并加密保存。再遍历找到已加密的pdf，并解密拷贝。

import os
import PyPDF2

os.chdir('..\\..\\Automate\\pdf')
for folders, subfolders, files in os.walk('.'):
    for file in files:
        fileReal = os.path.join(folders ,file)
        pdfNew = open(fileReal, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfNew)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        pdfFile = open(fileReal[:-4] + '_encrypted.pdf', 'wb')
        pdfWriter.encrypt('111111')
        pdfWriter.write(pdfFile)
        pdfNew.close()
        pdfFile.close()
