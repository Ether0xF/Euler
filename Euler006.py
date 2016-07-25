"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def sumSquareDiff(n = 10):
    # Formula to calculate the sum of an arithmetic series
    sq_sum = n * (n + 1) // 2
    # Special case of Faulhaber's Formula, square pyramidal numbers
    sum_sq = n * (n + 1) * (n * 2 + 1) // 6 
    return sq_sum ** 2 - sum_sq

if __name__ == '__main__':
    print("Sum Square Difference of from 1 to 10: {:d}".format(sumSquareDiff()))
    print("Sum Square Difference of from 1 to 100: {:d}".format(sumSquareDiff(100)))

