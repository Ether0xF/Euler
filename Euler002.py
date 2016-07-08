# By considering the terms in the Fibonacci sequence 
#whose values do not exceed four million, 
#find the sum of the even-valued terms.

a, b = 1, 1
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a+b
print(total)
