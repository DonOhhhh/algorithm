def dfs(matrix, n, count, x, y):
    matrix[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if matrix[nx][ny] == 1:
                count = dfs(matrix, n, count+1, nx, ny)
    return count

def main():
    n = int(input().replace('\ufeff',''))
    matrix = [list(map(int, input().replace('\ufeff',''))) for _ in range(n)]

    apartment_block = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                apartment_block.append(dfs(matrix, n, 1, i, j))
    print(len(apartment_block))
    for i in sorted(apartment_block): print(i)

if __name__ == '__main__':
    main()