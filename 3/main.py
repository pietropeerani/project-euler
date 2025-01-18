import math

def largest_prime_divisor(n):
    while n % 2 == 0:
        last_factor = 2
        n //= 2

    factor = 3
    max_possible_factor = math.isqrt(n)
    
    while factor <= max_possible_factor:
        while n % factor == 0:
            last_factor = factor
            n //= factor
            max_possible_factor = math.isqrt(n)
        factor += 2

    if n > 1:
        last_factor = n

    return last_factor

print(largest_prime_divisor(60085147514))

