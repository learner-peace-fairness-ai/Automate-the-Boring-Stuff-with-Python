from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

PASSWORD = 'swordfish'

with open('meetingminutes.pdf', 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
pdf_writer.encrypt(PASSWORD)
with open('encryptedminutes.pdf', 'wb') as result_pdf:
    pdf_writer.write(result_pdf)
