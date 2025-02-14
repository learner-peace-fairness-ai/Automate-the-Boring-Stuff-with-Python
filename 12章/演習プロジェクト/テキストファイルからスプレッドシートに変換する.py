# テキストファイルのテキスト行を各列に入力する
# Usage: python テキストファイルからスプレッドシートに変換する.py text_file1 text_file2 ...

import sys

from openpyxl import Workbook

EXCEL_FILENAME = 'テキストファイルからスプレッドシートに変換する.xlsx'

if len(sys.argv) < 2:
    print('Usage: python テキストファイルからスプレッドシートに変換する.py text_file1 text_file2 ...')
    sys.exit()

text_file_names = []
for file_name in sys.argv[1:]:
    text_file_names.append(file_name)

book = Workbook()
sheet = book.active

ci = 1
for file_name in text_file_names:
    with open(file_name, 'r', encoding='utf-8') as fr:
        ri = 1
        for line in fr.readlines():
            sheet.cell(row=ri, column=ci).value = line.rstrip()
            ri += 1
    ci += 1

book.save(EXCEL_FILENAME)
