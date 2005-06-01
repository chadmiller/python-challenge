
# http://www.pythonchallenge.com/pc/return/balloons.html
# brightness.html?
# deltas.gz

from gzip import GzipFile
text = GzipFile("data/deltas.gz").readlines()

left, right = [], []
for duo in (x.strip().split("   ") for x in text):
	left.append( "".join( [chr(int(x, 16)) for x in duo[0].split() ]) )
	if len(duo) > 1:
		right.append( "".join( [chr(int(x, 16)) for x in duo[1].split() ]) )


import difflib

d = difflib.Differ()
diff = list(d.compare(left, right))

file("left.png", "w").write( "".join([ x[2:] for x in diff if x.startswith("- ")]) )
file("right.png", "w").write( "".join([ x[2:] for x in diff if x.startswith("+ ")]) )
file("center.png", "w").write( "".join([ x[2:] for x in diff if x.startswith("  ")]) )

