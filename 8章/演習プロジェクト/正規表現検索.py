# フォルダの中のすべての　.txtファイル 内の　正規表現　にマッチする行を表示
# Usage:
# python 正規表現検索.py フォルダ 正規表現

import sys
import re
from pathlib import Path

folder = Path(sys.argv[1])
regex = re.compile(sys.argv[2])

text_files = [item for item in folder.iterdir() if item.is_file() and item.suffix == '.txt']
for text_file in text_files:
    with open(text_file, 'r', encoding='utf-8') as fr:
        lines = [line.rstrip() for line in fr.readlines()]

    for line in lines:
        if regex.search(line):
            print(line)