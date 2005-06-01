
# http://www.pythonchallenge.com/pc/hex/bin.html
# butter/fly

# Requires Python v2.4

from email import FeedParser
from base64 import b64decode
from StringIO import StringIO

parser = FeedParser.FeedParser()
parser.feed(file("data/binemail").read())
message = parser.close()

for part in message.walk():
	if part.get_content_type() == "audio/x-wav":
		file("please.wav", "w").write(b64decode(part.get_payload()))
	else:
		print "ignoring", part.get_content_type()


import wave
w = wave.open("please.wav", "r")


# Linux specific solution....
import ossaudiodev
dev = ossaudiodev.open("w")

dev.setfmt(ossaudiodev.AFMT_S16_BE)
dev.channels(1)
dev.speed(11025)

dev.write(w.readframes(w.getnframes()))
