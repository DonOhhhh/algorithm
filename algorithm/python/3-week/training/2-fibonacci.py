def fibonacci(n):
    if n<2: return n
    cache = [0 for _ in range(n+1)]
    cache[1] = 1
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

def fibonacci_dp(n):
    if n<2: return n
    cache = [0 for _ in range(n+1)]
    cache[1] = 1
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

def main():
    n = int(input().replace('\ufeff','').strip())
    print(fibonacci(n))
    print(fibonacci_dp(n))

if __name__=='__main__':
    main()