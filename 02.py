
# http://www.pythonchallenge.com/pc/def/ocr.html

import urllib
pageLines = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").readlines()
gibberish = "".join(pageLines[31:-1])

import re
print re.sub("[%s]" % re.escape("!@#$%^&*()_+[]{}\n\r"), "", gibberish)
