"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from operator import mul
from functools import reduce
import pdb

def pythagorean_triplet_product(num):
    """
    Find out the pythagorean triplet which have their sum equals to num.
    And then return the product of the triplet.

    Arguments: num -- the sum of the pythagorean triplet

    Result: product of pythagorean triplet.
    """
    def gcd(m, n):
        if n == 0:
            return m
        return gcd(n, m%n)

    def pythagorean_triplet(num):
        """
        Using Euclid's fomula to find out the pythagorean triplet.

        Arguments: num -- the sum of the pythagorean triplet goting to find out

        Result: a tuple contains the pythagorean triplet (a, b, c) 

        """
        a = 0
        b = 0
        c = 0

        m = 2   # coprime with n, therefore starts from 2
        n = 0
        k = 0   # coefficient in Euclid's fomula
        found = False

        while m < int((num//2) ** 0.5) and found != True:
            if(num // 2) % m == 0:
                n = 1 if m % 2 == 0 else 2
                while n < m and found != True:
                    if (num // 2 ) % (m + n) == 0 and gcd(m, n) == 1:
                        k = num // 2 // m // (m + n)
                        a = k * (m * m - n * n)
                        b = k * 2 * m * n
                        c = k * (m * m + n * n)
                        if (a + b + c) == num:
                            found = True
                    n += 1
            m += 1

        return (a, b, c)
    
    result = reduce(mul, pythagorean_triplet(num))
    return result

if __name__ == '__main__':
    print(pythagorean_triplet_product(1000))
