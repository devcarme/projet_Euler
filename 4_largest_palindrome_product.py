"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(n):
    palindrome = 1
    str_n = str(n)
    str_n_tuple = tuple(str_n)
    size = len(str_n_tuple)
    for i in range (size):
            if (str_n_tuple[i] != str_n_tuple[size-i-1]):
                palindrome = 0
            

                
    return palindrome

largest_palindrome = 0
for i in range(1000):
    for j in range(1000):
        if palindrome(i*j) and i*j > largest_palindrome:
            largest_palindrome = i*j
            

print(largest_palindrome)
        


   
                     
https://projecteuler.net/thread=4;page=8

import time

def loop():

    candidates = [0]
    for i in reversed(range(1000)):
        for j in reversed(range (1000)):

            current_number = i * j
            if current_number < max(candidates):
                break
            if str(current_number) == str(current_number)[::-1]:
                candidates.append(current_number)

    return(candidates)

tStart = time.time()
result = loop()
print(max(result))
print("run time = " + str((time.time() - tStart)))

de kpodsiadlo 
