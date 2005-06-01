# http://www.pythonchallenge.com/pc/return/uzi.html

import calendar

for year in xrange(1006, 2000, 10):
	if calendar.weekday(year, 01, 26) == calendar.MONDAY:
		print "Google for 26 January %d or one day later" % year
