from bisect import bisect
from copy import deepcopy

def lis_final(arr):
    lisArr = [0]
    for i in arr:
        if(i > lisArr[-1]):
            lisArr.append(i)
        elif(i < lisArr[-1]):
            x = bisect(lisArr,i)
            lisArr[x] = i
    return len(lisArr[1:])

def lis_recursive(arr,prev=-float('inf'),seq=[],result=[[]]):
    if(not arr): 
        return result
    for i in range(0,len(arr)):
        if(arr[i] <= prev): continue
        seq.append(arr[i])
        result = lis_recursive(arr[i+1:],arr[i],seq,result)
        # print(*seq)
        if(len(seq) >= len(result[-1])): result.append(deepcopy(seq))
        seq.pop()
    return result

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    # result = lis_final(arr)
    result = lis_recursive(arr)
    # print(result)
    print(len(result[-1]))

if __name__=='__main__':
    main()