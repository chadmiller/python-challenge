
# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
import sys

structure = pickle.load(file("data/banner.p"))

for row in structure:
	for char, count in row:
		sys.stdout.write(char * count)
	sys.stdout.write("\n")


#for row in structure:
#	print "".join([char * count for char, count in row])


#print "\n".join(["".join([char * count for char, count in row]) for row in pickle.load(file("data/banner.p"))])
