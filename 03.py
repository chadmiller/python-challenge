
# http://www.pythonchallenge.com/pc/def/equality.html

import urllib
pageLines = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").readlines()
gibberish = "".join(pageLines[31:-1])

import re
guarded_regexp = r"""(?x)  # turn on verbosity, so I can comment on each part
		(?<![A-Z])  # not preceeded by capital
		[A-Z]{3}
		( [a-z] )   # capture small letter
		[A-Z]{3}
		(?![A-Z])   # not followed by capital
		"""

smalls = re.findall(guarded_regexp, gibberish)

print "".join(smalls)
