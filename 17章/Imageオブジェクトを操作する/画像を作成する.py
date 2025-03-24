from PIL import Image

with Image.new('RGBA', (100, 200), 'purple') as img1:
    img1.save('purpleImage.png')

with Image.new('RGBA', (20, 20)) as img2:
    img2.save('transparentImage.png')    
