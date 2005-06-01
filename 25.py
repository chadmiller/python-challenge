
# http://www.pythonchallenge.com/pc/hex/lake.html
# butter/fly

import wave
import Image
import time

# 3600 = 60 * 60.  Hmmmm.
width, height = 60, 60
tiles_h, tiles_v = 5, 5

i = Image.new("RGB", (width*tiles_h,width*tiles_v))

for n in xrange(1,26):
	f = wave.open("data/lake%d.wav" % n, "r")

	for y in xrange(height):
		for x in xrange(width):
			i.putpixel((x+(width*((n-1)%tiles_h)),y+(height*((n-1)/tiles_v))), tuple(map(ord, f.readframes(3))))

	f.close()

i.show()
