from pathlib import Path

from PIL import Image

IMAGE_FILE = Path('../zophie.png')

with Image.open(IMAGE_FILE) as cat_img:
    cropped_img = cat_img.crop((335, 345, 565, 560))
    cropped_img.save('cropped.png')
