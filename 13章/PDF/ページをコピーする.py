from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

PDF_SOURCE_FILENAME_1 = 'meetingminutes.pdf'
PDF_SOURCE_FILENAME_2 = 'meetingminutes2.pdf'
PDF_OUTPUT_FILENAME = 'combinedminutes.pdf'

pdf_writer = PdfWriter()

with open(PDF_SOURCE_FILENAME_1, 'rb') as pdf_file1, open(PDF_SOURCE_FILENAME_2, 'rb') as pdf_file2:
    pdf_reader1 = PdfReader(pdf_file1)
    pdf_reader2 = PdfReader(pdf_file2)

    for page_num in range(len(pdf_reader1.pages)):
        page = pdf_reader1.pages[page_num]
        pdf_writer.add_page(page)
    
    for page_num in range(len(pdf_reader2.pages)):
        page = pdf_reader2.pages[page_num]
        pdf_writer.add_page(page)

with open(PDF_OUTPUT_FILENAME, 'wb') as pdf_output_file:
    pdf_writer.write(pdf_output_file)
