import heapq
n = int(input())
result = []
for _ in range(n):
    a,b = map(int, input().split())
    heapq.heappush(result,(b,a))
while result:
    b,a = heapq.heappop(result)
    print(a,b)