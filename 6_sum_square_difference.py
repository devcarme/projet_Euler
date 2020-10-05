"""
The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def difference(n):
    squares = 0
    for i in range(1,n+1):
        squares += i**2
    sum = 0
    for j in range(1,n+1):
        sum += j
    sum = sum**2
    
    return sum - squares

print(difference(100))


def problem6(r):
	return sum(r)** 2- sum([x** 2 for x in r])
problem6(range(1,101))
