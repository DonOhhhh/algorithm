# 201904014 Dong Joon Oh
def fibo(n):
    if n < 2: return n
    return fibo(n-2) + fibo(n-1) # 간단한 피보나치 수열 공식

print(fibo(int(input().replace('\ufeff',''))))