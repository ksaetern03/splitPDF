#!/usr/bin/python
import os

from PyPDF2 import PdfFileWriter, PdfFileReader

dirPath = os.path.dirname(os.path.realpath(__file__))

pdfdoc = "PDFFile.pdf"


fullPathToPDF = os.path.join(dirPath, pdfdoc)

inputpdf = PdfFileReader(open(fullPathToPDF , "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(dirPath+"/split/page_%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)