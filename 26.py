
# http://www.pythonchallenge.com/pc/hex/decent.html
# butter/fly

#From: Leopold Mozart <leopold.moz@pythonchallenge.com>
#To: pythchall@chad.org
#Date: 31-May-2005 18:25
#Subject: Re: Sorry
#
#Never mind that.
#
#Have you found my broken zip?
#
#md5: bbb8b499a0eef99b52c7f13f4e78c24b
#
#Can you believe what one mistake can lead to?


target = "bbb8b499a0eef99b52c7f13f4e78c24b"

import sys
import md5

contents = file("data/mybroken.zip", "r").read()

for i in xrange(len(contents)):
	for c in xrange(256):
		check = md5.new()
		check.update(contents[:i])
		check.update(chr(c))
		check.update(contents[i+1:])

		if check.hexdigest() == target:
			file("data/myfixed.zip", "w").write(contents[:i] + (chr(c) + contents[i+1:]))
			sys.exit()
