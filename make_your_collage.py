# Basic example that can be modified to make a perfect collage using python

from images2gif import writeGif
from PIL import Image
from random import randint
import os

file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))

images = [Image.open(fn).resize((520,520), Image.ANTIALIAS) for fn in file_names if fn != 'background.jpg']
print len(images)

back_image = Image.open("background.jpg") #choose a picture for background and name it as background.jpg
out = "collage.jpg"

row = 0
col = 0 # use this to set the index of images

for im in images:
		back_image.paste(im, (row,col))
		row = randint(0,1000) + 200 # use any randint() range you want
		col = randint(0,1000) + 200
	
back_image.save(out)

# Use this syntax to individually paste the images at your chosen location and then save it
# back_image.paste(images[1], (400,0))
# back_image.paste(images[2], (0,300))
# back_image.paste(images[3], (400,300))
	
# Make a GIF of your images, just uncomment below code

'''
print writeGif.__doc__
filename = "collage.GIF"
writeGif(filename, images, duration=0.1, dither=1)

'''