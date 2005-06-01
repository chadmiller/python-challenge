
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

import urllib

n = "12345"
format = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

while 1 == 1:
	page = urllib.urlopen(format % n).read()
	words = page.split()
	if len(words) >= 3 and words[-3] == "nothing" and words[-2] == "is":
		n = words[-1]
		print n
	elif "Divide by two" in page:
		n = str( int(n) / 2 )
		print n
	else:
		print page
		break
