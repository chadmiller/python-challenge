
# http://www.pythonchallenge.com/pc/return/evil.html
# huge/file
import Image

gfx = file("data/evil2.gfx").read()

n = 5   # Eyeballing looks like repetitions of 15.  "GIF" and "JFIF".
for i in range(n):
	name = "data/evil2-slice%d" % i
	file(name, "w").write(gfx[i::n])
	print "view", name
