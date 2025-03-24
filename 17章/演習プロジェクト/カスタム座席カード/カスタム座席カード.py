# "guests.txt"の招待客にカスタム座席カードの画像を生成する

from pathlib import Path

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

GUEST_FILE          = Path('guests.txt')
LOGO_FILE           = Path('catlogo.png')
SEATING_CARD_FOLDER = Path('座席カード')

with open(GUEST_FILE, encoding='utf-8') as fr:
    guests = [line.rstrip() for line in fr.readlines()]

with Image.open(LOGO_FILE) as logo_img:
    logo_width, logo_height = logo_img.size

    for guest in guests:
        # 座席カードをつくる
        with Image.new('RGBA', (288, 360), 'white') as img:  # サイズ 288 × 360
            draw = ImageDraw.Draw(img)
            width, height = img.size

            # 輪郭
            draw.line([(0, 0), (0, height - 1), (width - 1, height - 1), (width - 1, 0), (0, 0)], fill='black')
            
            # 来場者名
            meiryo_font = ImageFont.truetype('meiryo.ttc', size=35, index=0)  # メイリオ
            
            # 文字の位置が画像中央になるように指定
            left, top, right, bottom = draw.textbbox((0, 0), guest, font=meiryo_font)
            text_width  = right - left
            text_height = bottom - top
            draw.text((width/2 - text_width/2, height/2 - text_height/2), guest, fill='black', font=meiryo_font)
            
            # 装飾
            img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

            img.save(SEATING_CARD_FOLDER / f'{guest}.png')
