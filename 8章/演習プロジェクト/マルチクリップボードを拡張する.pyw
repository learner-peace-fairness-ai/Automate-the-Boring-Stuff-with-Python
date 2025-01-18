#! python3
# マルチクリップボードを拡張する.py - クリップボードのテキストを保存・復元
# USAGE:
# pythonw.exe マルチクリップボードを拡張する.pyw delete            - キーワードと紐づけられたテキストを全削除
# pythonw.exe マルチクリップボードを拡張する.pyw delete <keyword>  - キーワードと紐づけられたテキストを削除
# pythonw.exe マルチクリップボードを拡張する.pyw save <keyword>    - クリップボードをキーワードに紐づけて保存
# pythonw.exe マルチクリップボードを拡張する.pyw <keyword>         - キーワードに紐づけられたテキストをクリップボードにコピー
# pythonw.exe マルチクリップボードを拡張する.pyw list              - 全キーワードをクリップボードにコピー

import shelve
import sys

import pyperclip

command = sys.argv[1].lower()

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and command == 'save':
    key = sys.argv[2]
    mcb_shelf[key] = pyperclip.paste()
# キーワードと内容を削除
elif len(sys.argv) == 3 and command == 'delete':
    key = sys.argv[2]
    if key in mcb_shelf:
        del mcb_shelf[key]
elif len(sys.argv) == 2:
    # キーワード一覧と、内容の読み込み
    if command == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    # キーワードと内容をすべて削除
    elif command == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        key = sys.argv[1]
        pyperclip.copy(mcb_shelf[key])

mcb_shelf.close()