#! python3
# combinePdfs.py - カレントディレクトリの全PDFをひとつのPDFに結合する

from pathlib import Path

from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

OUTPUT_FILENAME = 'allminutes.pdf'

# すべてのPDFファイル名を取得する
pdf_files = [item for item in Path.cwd().iterdir() if item.is_file() and item.suffix == '.pdf']
pdf_files.sort(key=lambda p: p.name.lower())

pdf_writer = PdfWriter()

# すべてのPDFファイルをループする
for filename in pdf_files:
    with open(filename, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        # 先頭を除くすべてのページをループして追加する
        for page_num in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

# 結合したPDFをファイルに保存する
with open(OUTPUT_FILENAME, 'wb') as pdf_output:
    pdf_writer.write(pdf_output)
