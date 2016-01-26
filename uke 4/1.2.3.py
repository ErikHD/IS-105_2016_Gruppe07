#!/usr/bin/python
import collections
import string
from functools import partial

# uke04.py doesn't make that much sense parameter-wise, so just ignoring it
# and instead throwing stuff in sequentially here ...
# a) Se koden
# b) Se koden
# c) En bit "sløses", og man kunne slik sett kompaktet det mer.
#	 I prasis vil det dog være bedre å gzip-e, e.l. for å spare plass i
#	 overføring. For lagring vil man nok foretrekke å være kompatibel med andre
#	 løsninger, og derfor benytte veldefinerte ASCII eller UTF-8.

# Build ASCII-lookup table. Sure, it's stretching the task definition a bit ...
ASCIIEntry = collections.namedtuple('ASCIIEntry', ['letter', 'code'])
ascii_table = []

for c in string.printable:
	ascii_table.append(ASCIIEntry(c, "{:08b}".format(ord(c))))

target_string = ''
with open('sourcecode.txt', 'rb') as f:
	for ascii_code in iter(partial(f.read, 8), '\n'):
		# Find the corresponding letter
		match = next((x for x in ascii_table if x.code == ascii_code), None)
		if (match == None):
			print 'Could not find what we\'re looking for: ' + ascii_code
			exit()
		target_string += match.letter

# Decoded
print 'Decoding:'
print target_string

# Task told to encode as well ...
output_string = ''
for c in "Test string":
	match = next((x for x in ascii_table if x.letter == c), None)
	if not match:
		print 'Invalid letter'
		exit()
	output_string += match.code
print ''
print 'Encoding:'
print output_string
