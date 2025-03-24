from pathlib import Path

from PIL import Image

IMAGE_FILE = Path('../zophie.png')

with Image.open(IMAGE_FILE) as cat_img:
    print(cat_img.size)
    width, height = cat_img.size
    print(width)
    print(height)

    print(cat_img.filename)

    print(cat_img.format)

    print(cat_img.format_description)

    cat_img.save('zophie.jpg')    
