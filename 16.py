# http://www.pythonchallenge.com/pc/return/mozart.html

import Image

source = Image.open("data/mozart.gif")
pixels = source.getdata()

dest = source.resize((1400,600))
dest.paste(0, (0,0,1400,600))
x, y = 0, 0

history = [None] * 5
for i in xrange(len(pixels)):
	p = pixels[i]
	dest.putpixel( (x,y), p)
	x += 1

	if p!= history[0] and history[0] == history[1] == history[2] == history[3] == history[4]:
		x = 0
		y += 1

	history[i%5] = p
	
dest.show()
