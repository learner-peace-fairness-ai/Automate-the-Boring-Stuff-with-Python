from pathlib import Path

from PIL import Image

IMAGE_FILE = Path('../zophie.png')

with Image.open(IMAGE_FILE) as cat_img:
    thumb_img = cat_img.copy()
    print(thumb_img.size)

    thumb_img.thumbnail((100, 100))
    print(thumb_img.size)
    thumb_img.save('thumbnail.jpg')
