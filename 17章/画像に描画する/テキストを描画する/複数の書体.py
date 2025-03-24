from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

with Image.new('RGBA', (200, 200), 'white') as img:
    draw = ImageDraw.Draw(img)
    jfont = ImageFont.truetype('msmincho.ttc', 24, index=1)  # MS P明朝
    draw.text((20, 20), 'こんにちは', fill='black', font=jfont)

    jfont = ImageFont.truetype('msgothic.ttc', 24, index=2)  # MS Pゴシック
    draw.text((20, 50), 'こんにちは', fill='black', font=jfont)

    jfont = ImageFont.truetype('meiryo.ttc', 24, index=0)  # メイリオ
    draw.text((20, 80), 'こんにちは', fill='black', font=jfont)
    
    img.save('jtext.png')
