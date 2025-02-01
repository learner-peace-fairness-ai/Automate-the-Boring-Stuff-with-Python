#! python3
# mapIt.py - コマンドラインやクリップボードに指定した住所の地図を開く

import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:
    # コマンドラインから住所を取得する
    address = ' ' .join(sys.argv[1:])
else:
    # クリップボードから住所を取得する
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')
