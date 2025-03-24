from pathlib import Path

from PIL import Image

IMAGE_FILE = Path('../zophie.png')

with Image.open(IMAGE_FILE) as cat_img:
    cat_img.rotate(90).save('rotated90.png')
    cat_img.rotate(180).save('rotated180.png')
    cat_img.rotate(270).save('rotated270.png')

    cat_img.rotate(6).save('rotated6.png')
    cat_img.rotate(6, expand=True).save('rotated6_expanded.png')
