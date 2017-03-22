#! python3
# pdfMerge.py

import PyPDF2
import os

os.chdir('..\\..\\Automate')

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)

pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))       #叠加，首页打水印
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):        #首页之外正常拷贝
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfWriter.encrypt('abashing')     #PDF加密
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()