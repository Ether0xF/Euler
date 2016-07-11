"""
   A palindromic number reads the same both ways. 
   The largest palindrome made from the product of two 2-digit numbers is 
   9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers. 
"""
import math

# Function for judging if the given number is palindromic.
# Transform the number into string type and then reverse the string,
# would be a simple and quick solution to this problem as well.
def isPalindromic(num):
    if num < 0:
        return False
    
    divisor = 1
    while num // divisor >= 10:
        divisor *= 10
    
    while num != 0:
        left = num // divisor
        right = num % 10
        
        if left != right:
            return False
        else:
            num = num % divisor // 10
            divisor //= 100
    
    return True

def palindromicNumers(length = 3):
    p = list()

    for m in range(10 ** length - 1, 10 ** (length - 1) -1, -1):
        for n in range(m, 10 ** (length - 1) - 1, -1):
            if isPalindromic(m * n):
                p.append(m * n)

    return p

def largestPN(length = 3):
    return max(palindromicNumers(length))

if __name__ == '__main__':
    print(largestPN())

