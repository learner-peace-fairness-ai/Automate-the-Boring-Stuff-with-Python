#! python3
# ハードドライブの写真フォルダを探す.py - すべてのフォルダを調べて、「写真フォルダ」を探して絶対パスを表示する
#   写真フォルダ: フォルダ内のファイルの半分以上が「写真」であるフォルダ
#   写真: 拡張子が.pngまたは.jpgで、幅と高さが500以上の画像ファイル

from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path('C:\\')


def is_photo_folder(folder):
    num_photo_files = 0
    num_non_photo_files = 0

    for item in folder.iterdir():
        # .ファイル以外はカウントしない
        if not item.is_file():
            continue

        # .pngと.jpg以外は写真ではない
        elif item.suffix.lower() not in ('.png', '.jpg'):
            num_non_photo_files += 1
            continue

        # 幅と高さが500以上なら写真とする
        with Image.open(item) as img:
            width, height = img.size
            if width >= 500 and height >= 500:
                num_photo_files += 1
            else:
                num_non_photo_files += 1
    
    # ファイルの半分以上が写真なら写真フォルダとする
    if num_photo_files + num_non_photo_files == 0:
        return False
    else:
        return num_photo_files >= (num_photo_files + num_non_photo_files) / 2


photo_folders = []
if is_photo_folder(ROOT_FOLDER):
    photo_folders.append(ROOT_FOLDER.resolve())

for item in ROOT_FOLDER.rglob('*'):
    if item.is_dir():
        # 半分以上が写真なら
        if is_photo_folder(item):
            photo_folders.append(item.resolve())

for folder in photo_folders:
    print(folder.resolve())
