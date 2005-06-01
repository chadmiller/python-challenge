## Requires Python v2.4

# http://www.pythonchallenge.com/pc/return/romance.html
# huge/file

import urllib
import urllib2
import cookielib


n = "12345"
format = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"

jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
urllib2.install_opener(opener)


info = []
while 1 == 1:
	req = urllib2.Request(url=(format % n))
	jar.add_cookie_header(req)
	resp = urllib2.urlopen(req)
	jar.extract_cookies(resp, req)
	cookies = jar.make_cookies(resp, req)

	page = resp.read()

	c = cookies[0]
	info.append(urllib.unquote_plus(c.value))
	print c

	words = page.split()
	if len(words) >= 3 and words[-3] == "busynothing" and words[-2] == "is":
		n = words[-1]
		print n
	elif "Divide by two" in page:
		n = str( int(n) / 2 )
		print n
	else:
		print page
		break


import bz2
instructions =  bz2.decompress("".join(info))
print instructions
message = instructions.split('"')[1]
# He is Mozart.


message = "the flowers are on their way"

import xmlrpclib
server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.phone("Leopold")  # http://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart

# http://www.pythonchallenge.com/pc/return/violin.html sends us to...
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"

c.value = message
jar.set_cookie(c)

req = urllib2.Request(url=url)
resp = urllib2.urlopen(req)
page = resp.read()
cookies = jar.make_cookies(resp, req)

print page.split("\n")
print page.split("\n")[10]
