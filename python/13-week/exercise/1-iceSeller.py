INF = float('inf')

def checkBoundary(r,c,i,j):
    if((i < 0 or i >= r) or (j < 0 or j >= c)):
        return False
    else:
        return True

def iceRoad(r,c,w,m,i,j,visited):
    if(m[i][j]=='E'): return w

    dir = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]] # down,up,right,left
    for i,d in enumerate(dir):
        if(not checkBoundary(r,c,d[0],d[1])):
           dir[i] = 0

    weights = []
    for d in dir:
        if(d==0): 
            weights.append(INF)
        else:
            if(m[d[0]][d[1]] == 'S'):
                weights.append(INF)    
            elif(m[d[0]][d[1]] == 'E'):
                weights.append(-1)
            else:
                weights.append(m[d[0]][d[1]])
    
    minValue = INF
    minIndex = 0
    # 1. E와 가까운 쪽으로 먼저 이동
    # 2. E까지의 거리가 같은 두 노드 중 최솟값을 선택하여 진행
    # 3. E까지의 거리도 같도 값도 같다면 그냥 첫 번째를 선택
    while minValue == INF:
        minIndex = weights.index(min(weights))
        if(visited[dir[minIndex][0]][dir[minIndex][1]]):
            weights[minIndex] = INF
        else:
            minValue = weights[minIndex]
            visited[dir[minIndex][0]][dir[minIndex][1]] = True 
    if(minValue<0): minValue = 0
    return iceRoad(r,c,w-minValue,m,dir[minIndex][0],dir[minIndex][1],visited)

def main():
    r,c,w = map(int,input().split())
    matrix = [list(input()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            try:
                matrix[i][j] = int(matrix[i][j])
            except:
                pass
    v = [[False for _ in range(c)] for __ in range(r)]
    v[0][0] = True
    result = iceRoad(r,c,w,matrix,0,0,v)
    print(result)

if __name__=='__main__':
    main()