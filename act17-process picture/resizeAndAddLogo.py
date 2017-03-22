#! python3
# resizeAndAddLogo.py - resizes all images in current working directory to fit in a 300*300 square, and adds catlogo.png to the lower-right corner

import os
from PIL import Image

os.chdir('C:\\Users\\daize\\Desktop\\pythonTEST\\Automate')
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoIm = logoIm.resize((60, 80))
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
    # if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
    if not filename.endswith('phie.png') or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE/width)*height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height)*width)
            height = SQUARE_FIT_SIZE

        print('resizing %s...' % filename)
        im = im.resize((width, height))

    print('adding_logo to %s...' % filename)
    im.paste(logoIm, (width-logoWidth, height-logoHeight), logoIm)      #如果无第三个参数logoIm，则不会粘贴透明的像素
    im.save(os.path.join('withlogo', filename))     #.\\withlog\\filename
