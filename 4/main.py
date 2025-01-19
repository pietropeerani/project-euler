import math

def isPalindrome(n):
    for i in range(math.floor(len(n)/2)):
        if(n[i] != n[-i - 1]):
            return False
    return True

def largest_palindrome():
    result = 0
    for i in range(1000):
        for j in range(1000):
            if(isPalindrome(str(i*j))):
                result = max(result, i*j)
    return result

print(largest_palindrome())
