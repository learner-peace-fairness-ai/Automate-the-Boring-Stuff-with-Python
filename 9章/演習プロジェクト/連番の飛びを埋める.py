# フォルダ内の指定した接頭辞と接尾辞を持つ連番ファイルの番号の飛びを埋めるようにファイル名を変更する
# Usage:
# python 連番の飛びを埋める.py フォルダ 接頭辞 接尾辞

import os
from pathlib import Path
import re
import sys

SERIAL_NUMBER_DIGITS = 3  # 連番の桁数


def filter_sequential_files(file_list, prefix, suffix):
    regex = re.compile(fr'^{prefix}\d+\.{suffix}$')

    filterd_file_list = []
    for item in file_list:
        if not item.is_file():
            continue

        if regex.match(item.name):
            filterd_file_list.append(item)

    return filterd_file_list


if len(sys.argv) != 4:
    print('Usage: python 連番の飛びを埋める.py フォルダ 接頭辞 接尾辞')
    sys.exit()

search_dir = Path(sys.argv[1])
file_prefix = sys.argv[2]
file_suffix = sys.argv[3]

sequential_number = 1
file_list = [item for item in search_dir.iterdir() if item.is_file()]
sequential_file_list = filter_sequential_files(file_list, file_prefix, file_suffix)
sequential_number_regex = re.compile(r'\d+')
for file in sequential_file_list:
    mo = sequential_number_regex.search(file.name)
    num = int(mo.group())
    
    if num == sequential_number:
        sequential_number += 1
        continue
    
    new_filename = sequential_number_regex.sub(f'{sequential_number:03}', file.name)
    renamed_file = Path(file.parent)/new_filename
    os.rename(file, renamed_file)

    sequential_number += 1
