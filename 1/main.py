def multiples(n):
    result = []
    for i in range(n):
        if(i % 3 == 0 or i % 5 == 0):
            result.append(i)
    return result

def sum(arr):
    sum = 0;
    for item in arr:
        sum += item
    return sum

result = multiples(1000)
print(sum(result))
