from PyPDF2 import PdfReader

with open('meetingminutes.pdf', 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)
    
    print(len(pdf_reader.pages))

    page = pdf_reader.pages[0]
    print(page.extract_text())
