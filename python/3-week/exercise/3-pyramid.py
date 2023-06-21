# 201904014 Dong Joon Oh
def pascal(n):
    if n < 2: return 1
    return pascal(n-1) + 2**(n-1) # 피라미드의 모든 합이 파스칼의 삼각형의 수를 모두 더한 것과 같다.

if __name__=='__main__':
    n = int(input().replace('\ufeff',''))
    print(pascal(n))