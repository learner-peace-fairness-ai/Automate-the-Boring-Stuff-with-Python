# フォルダ内のサブフォルダも含めたすべてのPDFファイルをパスワードで暗号化する
# Usage: PDFをまとめて暗号化.py パスワード

from pathlib import Path
import sys

from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

ENCRYPTED_PDF_FILENAME_SUFFIX = '_encrypted.pdf'

if len(sys.argv) != 2:
    print('Usage: PDFをまとめて暗号化.py パスワード')
    sys.exit()
password = sys.argv[1]


def add_all_page(pdf_writer, pdf_file):
    with open(pdf_file, 'rb') as fr:
        pdf_reader = PdfReader(fr)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])


for pdf_file in Path.cwd().rglob('*.pdf'):
    pdf_writer = PdfWriter()
    add_all_page(pdf_writer, pdf_file)

    pdf_writer.encrypt(password)
    
    new_file = pdf_file.parent / f'{pdf_file.stem}{ENCRYPTED_PDF_FILENAME_SUFFIX}'
    with open(new_file, 'wb') as fw:
        pdf_writer.write(fw)

    with open(new_file, 'rb') as fr:
        pdf_reader = PdfReader(fr)
        if pdf_reader.decrypt(password):
            pdf_file.unlink()
        else:
            print(f'{pdf_file} の暗号化に失敗')
