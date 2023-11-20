#!/usr/bin/python3
import sys


def findFac(num):
	num = int(num)
	factor = 2
	while num % factor:
		if factor <= num:
			factor += 1
	return ((num // factor), factor)


if len(sys.argv) != 2:
	sys.exit("Usage: {0}: <filename>".format(sys.argv[0]))

factors = 0
filename = sys.argv[1]
with open(filename, "r") as fp:
	for i in fp:
		factors = findFac(i)
		print(f"{int(i)}={factors[0]}*{factors[1]}")
