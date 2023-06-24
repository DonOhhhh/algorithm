n = int(input())
result = [tuple(map(int, input().split())) for _ in range(n)]
result.sort(key=lambda x: (x[0], x[1]))
for x in result:
    print(x[0],x[1])