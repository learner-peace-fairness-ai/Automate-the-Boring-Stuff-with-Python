# フォルダ内のサブフォルダも含めたすべての暗号化されたPDFファイルをパスワードで復号化する
# Usage: PDFをまとめて復号化.py パスワード

from pathlib import Path
import sys

from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

ENCRYPTED_PDF_FILENAME_SUFFIX = '_encrypted.pdf'

if len(sys.argv) != 2:
    print('Usage: PDFをまとめて復号化.py パスワード')
    sys.exit()
password = sys.argv[1]


def add_all_page(pdf_writer, pdf_reader):
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])


def get_encrypted_filename(pdf_filename):
    list = pdf_filename.rsplit(ENCRYPTED_PDF_FILENAME_SUFFIX, maxsplit=1)
    return '.pdf'.join(list)


for pdf_file in Path.cwd().rglob(f'*{ENCRYPTED_PDF_FILENAME_SUFFIX}'):
    pdf_writer = PdfWriter()
    with open(pdf_file, 'rb') as fr:
        pdf_reader = PdfReader(fr)
        if not pdf_reader.is_encrypted:
            continue

        if not pdf_reader.decrypt(password):
            print(f'{pdf_file} のパスワードを解除できなかったのでスキップ')
            continue

        add_all_page(pdf_writer, pdf_reader)

    new_filename = get_encrypted_filename(pdf_file.name)
    new_file = pdf_file.parent / new_filename
    with open(new_file, 'wb') as fw:
        pdf_writer.write(fw)
    
    pdf_file.unlink()
