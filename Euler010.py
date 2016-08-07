"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import prime

lst = prime.sieve_era(2000000)
print(sum(lst))

