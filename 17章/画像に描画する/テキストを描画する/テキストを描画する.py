from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

with Image.new('RGBA', (200, 200), 'white') as img:
    draw = ImageDraw.Draw(img)
    draw.text((20, 150), 'Hello', fill='purple')
    arial_font = ImageFont.truetype('arial.ttf', 32)
    draw.text((100, 150), 'Howdy', fill='gray', font=arial_font)
    
    img.save('text.png')
