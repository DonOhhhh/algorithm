N, r, c = map(int, input().split())
cnt = 0
n = 2**N
grid = [[0] * n for _ in range(n)]
dxy = [(0, 0), (0, 1), (1, 0), (1, 1)]


def dfs(x, y, cur_n):
    global cnt, r, c
    for dx, dy in dxy:
        nx, ny = x + dx * 2**cur_n, y + dy * 2**cur_n
        grid[nx][ny] = cnt
        if cur_n - 1 >= 0:
            dfs(nx, ny, cur_n - 1)
            continue
        cnt += 1


dfs(0, 0, N-1)
print(grid[r][c])
