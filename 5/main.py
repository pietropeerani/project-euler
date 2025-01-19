def evenly_divisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

def smallest_divisible():
    n = 2520
    while(1):
        if(evenly_divisible(n)):
            return n
        n += 20

print(smallest_divisible())
