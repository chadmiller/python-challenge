
# http://www.pythonchallenge.com/pc/return/disproportional.html
# huge/file

import xmlrpclib

server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print server.phone("Bert")   # Bert is evil, says Google.
