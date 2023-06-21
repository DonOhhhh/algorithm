a,b = map(int,input().split())
def gcd(a,b):
    r = a%b
    return b if r == 0 else gcd(b,r)
print(gcd(a,b))