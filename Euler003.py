"""
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factor(num, prime_factor = 2):
    # refering prime factorization and factor tree.
    while prime_factor ** 2 <= num:
        if prime_factor ** 2 == num:
            return prime_factor
        else:
            while num % prime_factor == 0:
                num //= prime_factor
            prime_factor += 1
    
    return num

print(largest_prime_factor(600851475143))
