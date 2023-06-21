import math

def myListSort(li,w):
    if(len(li)==1): return li
    result = []
    left, right = li[:len(li)//2], li[len(li)//2:]
    while(left and right):
        if(w=='A'):
            if(left[0] <= right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif(w=='D'):
            if(left[0] >= right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
    
    result += left + right
    return result

def mergeSort(n,m,w,input_list):

    # index1 = insertElement1(n)
    # index2 = insertElement(n,[n],0)
    index3 = insertElement3([[0,n]],[0,n])

    cnt = 1

    for i in index3:
        tmp = myListSort(input_list[i[0]:i[1]],w)
        if(tmp!=input_list[i[0]:i[1]]):
            input_list[i[0]:i[1]] = tmp
            print(cnt,end=' : ')
            print(*input_list)
            # if(cnt==m): break
            cnt+=1
        
    return input_list

def insertElement1(n):
    fractions = [n]
    index = [fractions]
    # 
    while(not(1 in fractions)):
        # print(*fractions)
        tmp = []
        for i, frac in enumerate(fractions):
            tmp.append(frac//2)
            tmp.append(frac - frac//2)
        fractions = tmp.copy()
        index.append(tmp)
    return index

def insertElement2(n,arr,i):
    if(n//2==1):
        arr.insert(i,n//2)
        i = arr.index(n,i)
        arr.insert(i,math.ceil(n/2))
        return arr

    tmp1 = arr.index(n,i)
    arr.insert(tmp1,n//2)
    arr = insertElement2(n//2,arr,tmp1)

    i = tmp1
    tmp1 = arr.index(n,i)
    arr.insert(tmp1,math.ceil(n/2))
    arr = insertElement2(math.ceil(n/2),arr,tmp1)
    
    return arr

def insertElement3(arr,target):
    i = arr.index(target)
    start = arr[i][0]
    end = arr[i][1]
    if(end-start<=2): return arr
    arr.insert(i,[start,start+(end-start)//2])
    insertElement3(arr,[start,start+(end-start)//2])

    i = arr.index(target)
    arr.insert(i,[start+(end-start)//2,end])
    insertElement3(arr,[start+(end-start)//2,end])
    return arr

def main():
    n,m,w = input().replace('\ufeff','').split()
    input_list = list(input().replace('\ufeff','').split())
    print(*mergeSort(int(n),int(m),w,input_list))

if __name__=='__main__':
    main()