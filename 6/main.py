def square_of_sum(n):
    sum = (n*(n+1))/2
    return sum*sum

def sum_of_squares(n):
    return (1/6)*n*(n+1)*(2*n+1)

n = 100
print(square_of_sum(n) - sum_of_squares(n))
