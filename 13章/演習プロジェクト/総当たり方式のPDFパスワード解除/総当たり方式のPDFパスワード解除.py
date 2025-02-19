# ENCRYPTED_PDF_FILENAMEのパスワード解除をDICTIONARY_FILENAMEの単語の大文字・小文字で試して解除できたらパスワードを表示する

import sys

from PyPDF2 import PdfReader

ENCRYPTED_PDF_FILENAME = 'encrypted.pdf'
DICTIONARY_FILENAME    = 'dictionary.txt'

with open(DICTIONARY_FILENAME, encoding='utf-8') as fr:
    words = [line.rstrip() for line in fr.readlines()]

print('パスワード検索を開始...')
with open(ENCRYPTED_PDF_FILENAME, 'rb') as fr:
    reader = PdfReader(fr)

    for password in [word.lower() for word in words]:
        if reader.decrypt(password):
            print(f'パスワードを見つけました: {password}')
            sys.exit()
    
    for password in [word.upper() for word in words]:
        if reader.decrypt(password):
            print(f'パスワードを見つけました: {password}')
            sys.exit()

print('パスワードは見つかりませんでした')
