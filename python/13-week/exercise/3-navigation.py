from collections import defaultdict, deque
INF = float('inf')

def bfs(source, sink, parent, edge):
    visited = defaultdict(lambda: 0)
    queue = deque()
    queue.append(source)
    visited[source] = 1
    while queue:
        u = queue.popleft()
        for i in edge[u]:
            capacity = edge[u][i]
            if visited[i]:
                continue
            if capacity <= 0:
                continue
            queue.append(i)
            visited[i] = 1
            parent[i] = u
    if visited[sink]:
        return 1
    else:
        return 0

def min_flow(source, sink, parent, edge):
    flow  = INF
    while sink != source:
        flow = min(flow,edge[parent[sink]][sink])
        sink = parent[sink]
    return flow

def ford_fulkerson(source, sink, edge):
    parent = defaultdict(lambda:-1)
    max_flow = 0
    while bfs(source, sink, parent, edge):
        path_flow = min_flow(source, sink, parent, edge)
        max_flow += path_flow
        v = sink
        while v!=source:
            u = parent[v]
            edge[u][v] -= path_flow
            edge[v][u] += path_flow
            v = parent[v]
    return max_flow

def makeEdges(n,matrix):
    edges = []
    for i in range(n):
        for j in range(n):
            if(matrix[i][j]!=0):
                edges.append([str(i),str(j),matrix[i][j]])
    return edges

def main():
    n = int(input())
    s,t = str(0),str(n-1)
    matrix = [list(map(int,input().split())) for _ in range(n)]
    inputs = makeEdges(n,matrix)
    edge = defaultdict(lambda: defaultdict(int))

    for i,j,c in inputs:
        edge[i][j] += c
        edge[j][i] += c
    print(ford_fulkerson(s,t,edge))
    
if __name__=='__main__':
    main()