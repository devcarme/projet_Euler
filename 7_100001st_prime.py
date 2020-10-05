"""
10 001st prime
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

def th_prime(n):
    cpt=0
    i=1
    while (cpt < n):
        if is_prime(i):
            cpt+=1
        i+=1
    return i-1

print(th_prime(10001))


