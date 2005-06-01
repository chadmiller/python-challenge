
# http://www.pythonchallenge.com/pc/return/bull.html
# huge/file

def morris(n="1"):
	def gather(previous, next):
		if type(previous) != list:
			previous = [ [1, previous] ]

		if next == previous[-1][1]:
			previous[-1][0] += 1
		else:
			previous.append( [1, next] )

		return previous

	yield n
	
	# Special case -- reduce() won't work for a length-one sequence.
	if len(n) == 1:
		n = "%d%s" % (1, n)
		yield n

	while 1 == 1:
		n = "".join( [ "%d%s" % (pair[0], pair[1]) for pair in reduce(gather, n) ] )
		yield n


m = morris()
a = []

for i in range(31):
	a.append(m.next())

print len(a[30])

