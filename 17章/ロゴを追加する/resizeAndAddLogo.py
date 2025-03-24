#! python3
# resizeAndAddLogo.py - カレントディレクトリのすべての画像を
#                       300x300に収まるようにサイズ変更し、
#                       catlogo.pngを右下に追加する。

from pathlib import Path
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILE = Path('catlogo.png')
OUTPUT_DIR = Path('withLogo')

with Image.open(LOGO_FILE) as logo_img:
    logo_width, logo_height = logo_img.size

    OUTPUT_DIR.mkdir(exist_ok=True)

    # カレントディレクトリの全画像をループする
    for item in Path('.').iterdir():        
        if not item.is_file():
            continue
        elif item.suffix.lower() not in ('.png', '.jpg'):
            continue
        elif item.resolve() == LOGO_FILE.resolve():
            continue
        
        file = item
        with Image.open(file) as img:
            # 画像をサイズ変更する
            img.thumbnail((SQUARE_FIT_SIZE, SQUARE_FIT_SIZE))
            width, height = img.size

            # ロゴを追加する
            print(f'ロゴを追加中 {file.name}...')
            img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)
            
            # 変更を保存する
            img.save(OUTPUT_DIR / file.name)
