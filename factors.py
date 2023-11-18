#!/usr/bin/python3
import sys


def findFac(num):
	num = int(num)
	factor = 2
	while num != 0:
		if num % factor == 0:
			return (int(num / factor), factor)
		factor += 1


def main(filename):
	factors = 0
	with open(filename, "r") as fp:
		for i in fp:
			factors = findFac(i)
			print(f"{int(i)}={factors[0]}*{factors[1]}")


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: {0}: <filename>".format(sys.argv[0]))
	else:
		main(sys.argv[1])
