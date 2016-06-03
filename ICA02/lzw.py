#!/usr/bin/python
# -*- coding: utf-8 -*-

import struct
import array

def LZWCompress(data):
	string = ''
	dictionary = {}
	output = []
	for i in range(0, 256):
		dictionary[chr(i)] = i

	for char in data:
		if not string:
			string = char
			continue

		combined = string + char
		if combined in dictionary:
			string = string + char
			continue

		output.append(dictionary[string])
		dictionary[combined] = len(dictionary)
		string = char
	output.append(dictionary[string])
	return output

def LZWDecompress(data):
	element = ''
	dictionary = {}
	string = ''
	output = ''

	for i in range(0, 256):
		dictionary[i] = chr(i)

	for token in data:
		if not element:
			element = dictionary[token]
			output += element
			string = element
			continue

		string = string
		if token in dictionary:	element = dictionary[token]
		else: element = string + string[0]

		output += element
		dictionary[len(dictionary)] = string + element[0]
		string = element
	return output

action = ''

while action.lower() != 'compress' and action.lower() != 'decompress':
	action = raw_input('Compress or decompress?: ')

loadpath = raw_input('What file to load?: ')
storepath = raw_input('What file to store?: ')

data = ''
with open(loadpath) as f:
	data = f.read()

if action.lower() == 'compress':
	data = LZWCompress(data)
	with open(storepath, 'wb') as f:
		for b in data:
			f.write(struct.pack('H', b))
else:
	U = array.array('H')
	U.fromstring(data)
	data = LZWDecompress(U)

	with open(storepath, 'wb') as f:
		f.write(data)
