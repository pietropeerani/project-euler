import math

def is_prime(n):
    if n % 2 == 0:
        return False
    i = 3
    while i <= math.floor(math.sqrt(n) + 1):
        if n % i == 0:
            return False
        i += 2
    return True

def prime_number(n):
    count = 2
    prime = 3
    while count < n:
        prime += 2
        if is_prime(prime):
            count += 1
    return prime

print(prime_number(10001))
