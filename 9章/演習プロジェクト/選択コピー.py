# ディレクトリツリーを渡り歩いて、特定の拡張子のファイルを新しいフォルダにコピーする
# Usage:
# python 選択コピー.py 拡張子 検索フォルダ コピー先フォルダ

from pathlib import Path
import shutil
import sys

if len(sys.argv) != 4:
    print('Usage: python 選択コピー.py 拡張子 検索フォルダ コピー先フォルダ')
    sys.exit()

file_extension = sys.argv[1]
start_dir = Path(sys.argv[2])
dest_dir  = Path(sys.argv[3])

target_files = [item for item in start_dir.rglob(f'*{file_extension}')]

if not target_files:
    sys.exit()

if not dest_dir.exists():
    dest_dir.mkdir()

for file in target_files:
    shutil.copy(file, dest_dir)
