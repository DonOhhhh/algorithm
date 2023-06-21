from collections import deque

n,k = map(int, input().split())
people = deque(range(1,n+1))
result = []
while people:
    people.rotate(-(k-1))
    result.append(people.popleft())
print('<',end='')
print(*result,sep=', ',end='>')
