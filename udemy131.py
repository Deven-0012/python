import PyPDF2
f = open('first resume (1).pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)
f.close()