# 201904014 Dong Joon Oh
def euclid(dividend,divisor):
    if divisor==0: return dividend
    return euclid(divisor, dividend%divisor) # 제수를 피제수로 넣고 나머지 값을 제수로 넣어서 다시 한번 동작시킨다.

if __name__=='__main__':
    dividend, divisor = map(int,input().replace('\ufeff','').split())
    print(euclid(dividend,divisor))