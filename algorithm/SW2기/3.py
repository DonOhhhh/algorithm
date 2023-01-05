arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
limit = len(arr1) + len(arr2)
i = 0
j = 0
while i+j < limit:
    if i < len(arr1):
        print(arr1[i],end=' ')
        i += 1
    if j < len(arr2):
        print(arr2[j],end=' ')
        j += 1
    