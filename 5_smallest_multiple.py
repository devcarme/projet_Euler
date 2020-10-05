"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def is_prime(nb):
    if nb == 1:
        return False
    if nb == 2:
        return True
    elif nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

def smallest_number(n):
    tabPrime = []
    tabSmallest = []
    for i in range(n):
        if is_prime(i):
            tabPrime.append(i)
     
    print(tabPrime)

#print(smallest_number(20))

print(2*2*2*2*3*3*5*7*11*13*17*19)
