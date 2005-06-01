# http://www.pythonchallenge.com/pc/hex/bonus.html
# butter/fly

import os, urllib, sys
listpage = urllib.urlopen("http://www.python.org/doc/current/modindex.html").read()

print [x for x in os.listdir(sys.path[2]) if ">" + x.split('.',1)[0] + "<" not in listpage and ".pyc" not in x and ".pyo" not in x]

print "'this' looks neat.  Say -- that's in the title of the riddle page!"
print

import this

print
print "In the face of what?"
