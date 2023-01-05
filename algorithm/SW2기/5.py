row,col = map(int,input().split())
i,j,color = input().split()
i,j = int(i),int(j)
matrix = [list(input()) for _ in range(row)]
visited = [[False]*col for _ in range(row)]
originalColor = matrix[i][j]
direction = [(0,1),(1,0),(0,-1),(-1,0)]
def coloring(x,y):
    visited[x][y] = True
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < row and 0 <= ny < col) and (not visited[nx][ny]) and (matrix[nx][ny] == originalColor):
            coloring(nx,ny)
    matrix[x][y] = color
coloring(i,j)
for r in matrix:
    print(''.join(r))
