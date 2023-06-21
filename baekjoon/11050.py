def factorial(begin, end):
    result = 1
    for i in range(begin, end + 1):
        result *= i
    return result
n, k = map(int, input().split())
smallNum = min(n, n - k)
print(factorial(n - smallNum + 1, n) // factorial(1, smallNum))
