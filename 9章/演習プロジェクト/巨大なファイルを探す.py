# ディレクトリツリーを渡り歩いて、指定したファイルサイズより大きなファイルやフォルダの絶対パスを表示する
# Usage:
# python 巨大なファイルを探す.py フォルダ サイズ

from pathlib import Path
import sys

if len(sys.argv) != 3:
    print('Usage: python 巨大なファイルを探す.py フォルダ サイズ')
    sys.exit()

start_dir = Path(sys.argv[1])
file_size = int(sys.argv[2])

for item in start_dir.rglob('*'):
    if item.stat().st_size > file_size:
        print(item.resolve())
