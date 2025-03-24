from pathlib import Path

from PIL import Image

IMAGE_FILE = Path('../zophie.png')

with Image.open(IMAGE_FILE) as cat_img:
    cat_img.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
    cat_img.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
