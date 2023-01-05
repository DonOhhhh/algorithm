def func(x):
    return int(x)**2
result = sum(list(map(func,input().split()))) % 10
print(result)