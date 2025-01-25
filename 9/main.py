def find_pythagorean_triplet(sum_value):
    for a in range(1, sum_value // 2):
        for b in range(a + 1, sum_value // 2):
            c = sum_value - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
    return None

sum_value = 1000

a, b, c = find_pythagorean_triplet(sum_value)

product = a * b * c
print(product)
