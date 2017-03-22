import PyPDF2
import os

os.chdir('..\\..\\Automate')

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1 = PyPDF2.PdfFileReader(pdf1File)
pdf2 = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()      #表示一个空白PDF文档

for pageNum in range(pdf1.numPages):        #range()默认从0开始
    pageObj = pdf1.getPage(pageNum)
    pdfWriter.addPage(pageObj)      #将page对象传递给pdfWriter

for pageNum in range(pdf2.numPages):
    pageObj = pdf2.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutFile = open('combine.pdf', 'wb')
pdfWriter.write(pdfOutFile)
pdfOutFile.close()
pdf1File.close()
pdf2File.close()