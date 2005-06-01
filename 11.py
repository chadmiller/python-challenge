
# http://www.pythonchallenge.com/pc/return/5808.html
# huge/file

import Image

source = Image.open("data/cave.jpg")

destOne = Image.new(source.mode, source.size)
destTwo = Image.new(source.mode, source.size)

width, height = source.size

for y in range(height):
	for x in range(width):
		pixel = source.getpixel((x,y))
		if (x + y) % 2 == 0:
			destOne.putpixel((x,y), pixel)
			destTwo.putpixel((x,y), (0,0,0))
		else:
			destOne.putpixel((x,y), (0,0,0))
			destTwo.putpixel((x,y), pixel)


destOne.show()
destTwo.show()
