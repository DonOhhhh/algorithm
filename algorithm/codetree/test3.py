from collections import deque

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dxy = [(1,0),(0,1),(-1,0),(0,-1)]
q = deque()

def can_go(x,y):
    if not (n > x >= 0 and m > y >= 0):
        return False
    if not matrix[x][y]:
        return False
    if visited[x][y]:
        return False
    if (x,y) in q:
        return False
    return True

q.append((0,0))

while q:
    x,y = q.popleft()
    visited[x][y] = 1
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if can_go(nx,ny):
            q.append((nx,ny))

print(visited[n-1][m-1])