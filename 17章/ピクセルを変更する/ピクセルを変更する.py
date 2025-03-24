from PIL import Image
from PIL import ImageColor

with Image.new('RGBA', (100, 100)) as img:
    pixcel = img.getpixel((0, 0))
    print(pixcel)

    for y in range(50):
        for x in range(100):
            img.putpixel((x, y), (210, 210, 210))

    darkgray = ImageColor.getcolor('darkgray', 'RGBA')
    for y in range(50, 100):
        for x in range(100):
            img.putpixel((x, y), darkgray)
    
    pixcel = img.getpixel((0, 0))
    print(pixcel)

    pixcel = img.getpixel((0, 50))
    print(pixcel)

    img.save('putPixcel.png')
