from pathlib import Path

from PIL import Image

IMAGE_FILE = Path('../zophie.png')

with Image.open(IMAGE_FILE) as cat_img:
    width, height = cat_img.size
    quartersized_img =  cat_img.resize((int(width / 2), int(height / 2)))
    quartersized_img.save('quartersized.png')

    svelte_img = cat_img.resize((width, height + 300))
    svelte_img.save('svelte.png')
