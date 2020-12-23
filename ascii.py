from PIL import Image, ImageDraw, ImageFont

import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars = "#Wo- "[::-1]
charkafası = list(chars)
charLength = len(charkafası)
interval = charLength/256

scaleFactor = 0.09

oneCharWidth = 10
oneCharHeight = 18

def getCHAR(inputInt):
    return charkafası[math.floor(inputInt*interval)]
# This one text output of your image
text_file = open("Output.txt", "w")
# You must append your image to idle and write your image name down
im = Image.open("yourimage.png")

font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pixel = im.load()
# RGB = red green blue you can easily change color part between 0-255
outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        pixel[j,i]
        r, g, b = pixel[j, i]
        h = int(r/3 + g/3 + b/3)
        pixel[j, i] = (h, h, h)
        text_file.write(getCHAR(h))
        d.text((j*oneCharWidth, i*oneCharHeight), getCHAR(h), font = font, fill = (r, g, b))

    text_file.write('\n')
# This code below will print your output image and save as a output.png 
outputImage.save('output.png')
