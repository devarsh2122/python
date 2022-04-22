#Import required library
from PIL import Image

#Open Image
im = Image.open("TajMahal.jpg")

#Image rotate & show
im.show()
im.rotate(45).show()
im.rotate(90).show()
im.rotate(180).show()
im.rotate(270).show()
