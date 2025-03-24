from pathlib import Path

from PIL import Image

IMAGE_FILE = Path('../zophie.png')

with Image.open(IMAGE_FILE) as cat_img:
    face_img = cat_img.crop((335, 345, 565, 560))
    
    cat_img_width, cat_img_height   = cat_img.size
    face_img_width, face_img_height = face_img.size

    cat_copy_img = cat_img.copy()
    for left in range(0, cat_img_width, face_img_width):
        for top in range(0, cat_img_height, face_img_height):
            print(left, top)
            cat_copy_img.paste(face_img, (left, top))
    
    cat_copy_img.save('tiled.png')
