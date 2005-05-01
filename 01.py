# http://www.pythonchallenge.com/pc/def/map.html

import string

encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

rotation = ord('m') - ord('k')

source_alphabet = string.lowercase  # all lowercase letters.  We assume they are in order.
destination_alphabet = string.lowercase[rotation:] + string.lowercase[:rotation]   # rot=3  "defghxyz" + "abc"

print encrypted.translate(string.maketrans(source_alphabet, destination_alphabet))
print "url:", "map".translate(string.maketrans(source_alphabet, destination_alphabet))
