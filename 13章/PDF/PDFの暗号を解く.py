from PyPDF2 import PdfReader
from PyPDF2.errors import FileNotDecryptedError

PASSWORD = 'rosebud'

with open('encrypted.pdf', 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    print(pdf_reader.is_encrypted)

    try:
        pdf_reader.pages[0]
    except FileNotDecryptedError as e:
        print(e)
    
    pdf_reader.decrypt(PASSWORD)
    page = pdf_reader.pages[0]
    print('パスワード解除')
