
# http://www.pythonchallenge.com/pc/hex/speedboat.html
# butter/fly

import Image
import ImagePalette

repetition = 99

source = Image.open("data/zigzag.gif", "r")

#dest = Image.new(source.mode, source.size)

pal = source.palette.getdata()

pixel_data = source.getdata()

captured = []
try:
	for index, color in enumerate(pixel_data):
		deref = ord(pal[1][color*3])
		if deref == pixel_data[index-1]:
			print index
			captured.append(0)
		elif deref == pixel_data[index+1]:
			captured.append(1)
		else:
			pass

except IndexError:
	pass


print captured
