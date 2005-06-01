import zlib
import bz2

file_name = "data/21/package.pack"

packed_contents = file(file_name).read()

sequence = list()
i = 0
while 1 == 1:
	if packed_contents[:2] == "BZ":
		packed_contents = bz2.decompress(packed_contents)
		sequence.append("B")
	else:
		try:
			try:
				packed_contents = zlib.decompress(packed_contents)
				sequence.append("-")
			except zlib.error:
				packed_contents = zlib.decompress(packed_contents[::-1])
				sequence.append("\n")

		except zlib.error:
			contents = packed_contents
			break

	i += 1

print contents[::-1]
print "".join(sequence)


