def getMaxHeight(start, end, m, trees):
    mid = end
    while end >= start:
        length = sum(list(map(lambda x: x - mid if (x - mid) > 0 else 0, trees)))
        if length == m:
            break
        elif length < m:
            end = mid - 1
        else:
            start = mid + 1
        mid = (end + start) // 2
    return mid


n, m = map(int, input().split())
trees = list(map(int, input().split()))
result = getMaxHeight(0, max(trees), m, trees)
print(result)
