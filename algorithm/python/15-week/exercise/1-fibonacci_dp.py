def fibo(n):
    cnt = 2
    arr = [0,1]
    while cnt<=n:
        arr.append(arr[cnt-1]+arr[cnt-2])
        cnt+=1
    return arr[-1]

print(fibo(int(input())))