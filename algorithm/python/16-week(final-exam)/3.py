import math

def rollingBid(n,m,pos,dst,maze,visited):
    
    if(pos[0] < 0 or pos[0] >= n): return 'switch'
    if(pos[1] < 0 or pos[1] >= m): return 'switch'
    if(math.sqrt(pow(abs(pos[0]-dst[0]),2) + pow(abs(pos[1]-dst[1]),2)) == 0): return 'end'
    if(maze[pos[0]][pos[1]] == 1): return 'switch'
    if(visited[pos[0]][pos[1]] == 1): return 'visited'
    
    visited[pos[0]][pos[1]] = 1
    result = rollingBid(n,m,[pos[0]+1,pos[1]],dst,maze,visited)  
        
    return visited

def main():
    n,m = map(int,input().split())
    src = list(map(int,input().split()))
    dst = list(map(int,input().split()))
    maze = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0 if(maze[i][j] == 0) else 2
    print(maze[0])
    # print(rollingBid(n,m,src,dst,maze,visited))

if __name__=='__main__':
    main()