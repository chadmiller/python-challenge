
# http://www.pythonchallenge.com/pc/def/oxygen.html

import Image  #this is from PIL, the Python Imaging Library. Debian pkg "python-imaging".
import sys

image = Image.open("data/oxygen.png")

# the stripe goes down the center, and each block is 7 pixels wide
width, height = image.size
y = height / 2
for x in range(0, width, 7):
	r,g,b,a = image.getpixel( (x, y) )
	if r == g and g == b:
		sys.stdout.write(chr(r))

sys.stdout.write("\n")

print "".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
