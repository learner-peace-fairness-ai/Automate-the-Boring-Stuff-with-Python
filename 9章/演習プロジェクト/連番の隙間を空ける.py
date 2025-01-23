# 指定した連番ファイルを入れられるように、フォルダ内の連番ファイルの「連番」を変更する
# Usage:
# python 連番の隙間を空ける.py フォルダ 連番ファイル

import os
from pathlib import Path
import re
import sys


def filter_sequential_files(file_list, prefix, suffix):
    regex = re.compile(fr'^{prefix}\d+\.{suffix}$')

    filterd_file_list = []
    for item in file_list:
        if not item.is_file():
            continue

        if regex.match(item.name):
            filterd_file_list.append(item)

    return filterd_file_list


if len(sys.argv) != 3:
    print('Usage: python 連番の隙間を空ける.py フォルダ 連番ファイル')
    sys.exit()

search_dir      = Path(sys.argv[1])
sequential_file = Path(sys.argv[2])

sequential_number_filename_regex = re.compile(r'(^\D+)(\d+)\.(\D+)$')
mo = sequential_number_filename_regex.search(sequential_file.name)
file_prefix = mo.group(1)
file_suffix = mo.group(3)
sequential_number = mo.group(2)

file_list = [item for item in search_dir.iterdir() if item.is_file()]
sequential_file_list = filter_sequential_files(file_list, file_prefix, file_suffix)

if not search_dir/sequential_file in sequential_file_list:
    sys.exit()

sequential_number_regex = re.compile(r'\d+')
sequential_file_list.sort(reverse=True)
for file in sequential_file_list:
    mo = sequential_number_regex.search(file.name)
    num = mo.group()
    new_num = int(num) + 1

    new_filename = sequential_number_regex.sub(f'{new_num:03}', file.name)
    renamed_file = Path(file.parent)/new_filename
    os.rename(file, renamed_file)
    
    if num == sequential_number:
        break
