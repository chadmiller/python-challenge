
# http://www.pythonchallenge.com/pc/return/italy.html
# huge/file

import Image

source = Image.open("data/wire.png")
dest = Image.new(source.mode, (100,100) )

i = 0
for ring in xrange(100/2):
	stop = 100-ring
	for n in xrange(ring, stop-1):
		dest.putpixel( (n, ring), source.getpixel((i,0)))
		i += 1
	for n in xrange(ring, stop-1):
		dest.putpixel( (stop-1, n), source.getpixel((i,0)))
		i += 1
	for n in xrange(ring, stop-1):
		dest.putpixel( (100-n-1, stop-1), source.getpixel((i,0)))
		i += 1
	for n in xrange(ring, stop-1):
		dest.putpixel( (ring, 100-n-1), source.getpixel((i,0)))
		i += 1

dest.show()
