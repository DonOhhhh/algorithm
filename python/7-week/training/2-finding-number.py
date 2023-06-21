# 순차 검색
# 정렬 후 이진 검색 √
# 해시
import bisect

def findingNumber(n,bl,m,sl):
    result = []
    bl = sorted(bl)
    for i in sl:
        j = bisect.bisect(bl,i)
        if(i == bl[j-1]):
            result.append(1)
        else:
            result.append(0)

    return result

def main():
    n = int(input().replace('\ufeff',''))
    base_list = list(map(int,input().replace('\ufeff','').split()))
    m = int(input().replace('\ufeff',''))
    search_list = list(map(int,input().replace('\ufeff','').split()))
    result = findingNumber(n,base_list,m,search_list)
    [print(x) for x in result]

if __name__=='__main__':
    main()