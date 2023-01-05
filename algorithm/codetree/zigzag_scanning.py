n, m = map(int, input().split())
# dx,dy = tuple(zip(*[(0,1),(1,-1),(1,0),(-1,1)]))
dx, dy = tuple(zip(*[(1, 0), (-1, 1), (0, 1), (1, -1)]))
cur_dir = 0
prev_dir = 1
x, y = 0, 0
matrix = [[0] * m for _ in range(n)]
matrix[0][0] = 1
cnt = 2
while cnt <= n * m:
    if not prev_dir % 2:
        cur_dir = (cur_dir + 1) % 4
    while True:
        nx, ny = x + dx[cur_dir], y + dy[cur_dir]
        prev_dir = cur_dir
        if n > nx >= 0 and m > ny >= 0 and matrix[nx][ny] == 0:
            break
        cur_dir = (cur_dir + 1) % 4
    x, y = nx, ny
    matrix[x][y] = cnt
    cnt += 1
for r in matrix:
    for c in r:
        print(f"{c:02d}", end=" ")
    print()
