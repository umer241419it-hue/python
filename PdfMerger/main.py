import PyPDF2

pdfiles = [r"Pdfmerger\file1.pdf", r"Pdfmerger\file2.pdf", r"Pdfmerger\file3.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
  pdfFile = open(filename, 'rb')
  pdfReader = PyPDF2.PdfReader(pdfFile)
  merger.append(pdfReader)
pdfFile.close()
merger.write(r"Pdfmerger\merged.pdf")