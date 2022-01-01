from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

def factorial(n):
    if n<2: return 1
    return factorial(n-1)*n

def main():
    n = int(input().replace('\ufeff','').strip())
    print(factorial(n))
    print(factorial_reduce(n))

if __name__=='__main__':
    main()