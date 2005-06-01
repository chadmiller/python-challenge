# http://www.pythonchallenge.com/pc/hex/copper.html
# butter/fly

import Image
import ImageSequence

source = Image.open("data/white.gif")

seq = ImageSequence.Iterator(source)
dest = Image.new("RGB", (200,200))

tx, ty = 20, 100

for i in xrange(134):
	try:
		im = seq[i]
	except IndexError:
		break

	d = list(im.getdata())
	offset = d.index(8)   # 8 is the color we're interested in

	x, y = offset%200, offset/200

	if (x,y) == (100,100):
		tx += 20
		continue

	if x == 102:
		tx += 1
	elif x == 98:
		tx -= 1
	elif x == 100:
		pass
	else:
		raise ValueError, x

	if y == 102:
		ty += 1
	elif y == 98:
		ty -= 1
	elif y == 100:
		pass
	else:
		raise ValueError, y

	dest.putpixel( (tx, ty), 0xffffff)

dest.show()
