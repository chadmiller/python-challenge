
# http://www.pythonchallenge.com/pc/def/channel.html

import zipfile
import sys

n = "90052"

zip = zipfile.ZipFile("data/channel.zip")

while 1 == 1:
	filename = "%s.txt" % n
	sys.stdout.write(zip.getinfo(filename).comment)
	words = zip.read(filename).split()
	assert words[-3:-1] == ["nothing", "is"]
	n = words[-1]
	


