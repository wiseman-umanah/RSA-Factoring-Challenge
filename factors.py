#!/usr/bin/python3
import sys
import random


def pollard_rho(n):
    if n % 2 == 0:
        return 2

    x = random.randrange(2, n)
    y = x
    d = 1

    while d == 1:
        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n
        d = gcd(abs(x - y), n)

    if d == n:
        return n
    else:
        return d

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if len(sys.argv) != 2:
    sys.exit(f"Usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    num = int(line.rstrip())
    factor = pollard_rho(num)
    print(f"{num}={num//factor}*{factor}")
