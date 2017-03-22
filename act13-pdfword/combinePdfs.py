#! python3
# combinePdfs.py - combines all the PDFs in the current working directory info a single PDF

import PyPDF2
import os

lst = []
os.chdir('..\\..\\Automate')
lstAutomate = os.listdir()
for i in lstAutomate:
    if i.endswith('.pdf'):
        lst.append(i)
lst.sort(key=str.lower)     #以字母字典顺序排序

pdfWriter = PyPDF2.PdfFileWriter()

for i in lst:
    pdfFile = open(i, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    for j in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(j)
        pdfWriter.addPage(pageObj)

pdfOut = open('all.pdf', 'wb')
pdfWriter.write(pdfOut)
pdfOut.close()
