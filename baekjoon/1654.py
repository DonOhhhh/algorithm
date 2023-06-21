def getMaxLength(begin, end, n, ropes):
    mid = end
    while end >= begin:
        ropeNum = sum(list(map(lambda rope : rope // mid, ropes)))
        if ropeNum < n:
            end = mid - 1
        elif ropeNum >= n:
            begin = mid + 1
        mid = (end + begin) // 2
    return mid
        
k,n = map(int, input().split())
ropes = [int(input()) for _ in range(k)]
result = getMaxLength(1,max(ropes), n, ropes)
print(result)