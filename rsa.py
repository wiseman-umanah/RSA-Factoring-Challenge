#!/usr/bin/python3
import sys
import random


def pollard_rho(n):
    if n == 1:
        return n
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
        return None
    else:
        return d

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if len(sys.argv) != 2:
    sys.exit(f"Usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

with open(filename, "r") as fp:
    i = fp.read()
    i = int(i)
    fac1 = pollard_rho(i)
    if fac1 == None:
         sys.exit(f"{i} must not be a prime number or 1")
    else:
        fac2 = pollard_rho(i//fac1)
        if fac2 == None:
            fac2 = i//fac1
            print(f"{i}={fac2}*{fac1}")
        else:
            sys.exit("n=p*q, where p and q are prime numbers")