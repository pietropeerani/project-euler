def fibonacci(n):
    result = []
    value = 2
    prev_value = 1
    while(value < n):
        if(value % 2 == 0):
            result.append(value)
        tmp = value
        value += prev_value
        prev_value = tmp
    return result

def sum(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum

print(sum(fibonacci(4000000)))
