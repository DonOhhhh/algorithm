n = int(input())
for _ in range(n):
    x = int(input())
    arr = list(range(x+1))
    arr[0] = (1,0)
    try:
        arr[1] = (0,1)
        for i in range(2,x+1):
            arr[i] = (lambda a,b: (a[0]+b[0],a[1]+b[1]))(arr[i-1],arr[i-2])
    except IndexError:
        pass
    print(*arr[x])
