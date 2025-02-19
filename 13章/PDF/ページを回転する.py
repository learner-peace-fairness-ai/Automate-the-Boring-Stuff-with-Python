from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

with open('meetingminutes.pdf', 'rb') as minutes_file, open('rotatedPage.pdf', 'wb') as result_pdf_file:
    pdf_reader = PdfReader(minutes_file)
    page = pdf_reader.pages[0]
    page.rotate(90)

    pdf_writer = PdfWriter()
    pdf_writer.add_page(page)
    pdf_writer.write(result_pdf_file)
