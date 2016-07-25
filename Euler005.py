"""
    2520 is the smallest number that can be divided
    by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?

"""
import prime
from math import log

def lcm(m, n):
    return m * (n // gcd(m, n))

def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)

def smallestLCM(f = 1, t = 10):
    x = 1
    for i in range(f, t + 1):
        x = lcm(x, i)

    return x

def smallest_lcm(f = 1, t = 10):
    primes = prime.sieve_era(t)
    result = 1

    for p in primes:
        power = log(t) // log(p) if p <= t ** 0.5 else 1
        result *= int(p ** power)
    return result


if __name__ == '__main__':
    #print("Smallest LCM from 1 to 10: {:d}".format(smallestLCM()))
    #print("Smallest LCM from 1 to 20: {:d}".format(smallestLCM(1, 20)))
    print("Smallest LCM from 1 to 10: {:d}".format(smallest_lcm()))
    print("Smallest LCM from 1 to 20: {:d}".format(smallest_lcm(1, 20)))
