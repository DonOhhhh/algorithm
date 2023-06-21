from copy import deepcopy
import sys

sys.setrecursionlimit(10**6)

dxy = [(0,1),(1,0),(0,-1),(-1,0)]

def in_range(x,y):
    global n,m
    return (n > x >= 0 and m > y >= 0)

def dfs(x,y):
    global visited
    visited[x][y] = 1
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if in_range(nx,ny) and not visited[nx][ny] and grid[nx][ny]:
            dfs(nx,ny)

T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())
    grid = [[0]*m for ___ in range(n)]
    visited = deepcopy(grid)
    cnt = 0
    for __ in range(k):
        c,r = map(int,input().split())
        grid[r][c] = 1
    for x in range(n):
        for y in range(m):
            if grid[x][y] and not visited[x][y]:
                dfs(x,y)
                cnt+=1
    print(cnt)
        
    