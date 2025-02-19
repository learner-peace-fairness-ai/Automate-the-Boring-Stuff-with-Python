from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

with open('meetingminutes.pdf', 'rb') as minutes_file, open('watermark.pdf', 'rb') as watermark_file:
    pdf_watermark_reader = PdfReader(watermark_file)
    watermark_first_page = pdf_watermark_reader.pages[0]
    
    pdf_reader = PdfReader(minutes_file)
    minutes_first_page = pdf_reader.pages[0]
    minutes_first_page.merge_page(watermark_first_page)

    pdf_writer = PdfWriter()
    pdf_writer.add_page(minutes_first_page)
    for page_num in range(1, len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

with open('watermarkedCover.pdf', 'wb') as result_pdf_file:
    pdf_writer.write(result_pdf_file)
