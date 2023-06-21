# 이진 검색
def immigrationTest(m,times):
    start = 1
    end = max(times)*m
    result = 0
    
    while(end>=start):
        mid = (end+start)//2
        if(sum([mid//i for i in times]) < m):
            start = mid+1
        else:
            end = mid-1
            result = mid

    return result
 
def main():
    n,m = map(int,input().replace('\ufeff','').split())
    times = [int(input().replace('\ufeff','')) for x in range(n)]
    result = immigrationTest(m,times)
    print(result)

if __name__=='__main__':
    main()