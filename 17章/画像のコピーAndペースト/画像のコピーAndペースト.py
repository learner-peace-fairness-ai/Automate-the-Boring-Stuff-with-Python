from pathlib import Path

from PIL import Image

IMAGE_FILE = Path('../zophie.png')

with Image.open(IMAGE_FILE) as cat_img:
    cat_copy_img = cat_img.copy()

    face_img = cat_img.crop((335, 345, 565, 560))
    print(face_img.size)

    cat_copy_img.paste(face_img, (0, 0))
    cat_copy_img.paste(face_img, (400, 500))
    cat_copy_img.save('pasted.png')
