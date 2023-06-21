#201904014 Dong Joon Oh
import collections

# collections.Counter 메소드를 이용하여 해당 배열에서 각각의 키 별로 몇개인지 세서 dictionary로 돌려줌.
# 돌려받은 dictionary의 차를 구해서 해당 값의 key값을 돌려줌.
def compareCollections(p,c):
    i = collections.Counter(p) - collections.Counter(c)
    return list(i.keys())

def main():
    a = input().replace('\ufeff','').split()
    b = input().replace('\ufeff','').split()
    print(*compareCollections(a,b))

if __name__=='__main__':
    main()