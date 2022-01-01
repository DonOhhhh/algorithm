import sys,collections
import heapq
from copy import deepcopy

def makeGraphDict(edges):
    graph = {}
    
    for e in edges:
        if(e[0] in graph.keys()): graph[e[0]][e[1]] = int(e[2])
        else: graph[e[0]] = {e[1]:int(e[2])}
        if(e[1] in graph.keys()): graph[e[1]][e[0]] = int(e[2])
        else: graph[e[1]] = {e[0]:int(e[2])}
    return graph

def makeGraphList(edges):
    # 각 노드마다 연결된 모든 노드의 정보를 graph에 입력한다.
    # 무방향이기 때문에 2번 입력해준다.
    graph = {}
    
    for e in edges:
        if(e[0] in graph.keys()): graph[e[0]].append([int(e[2]),e[1]])
        else: graph[e[0]] = [[int(e[2]),e[1]]]
        if(e[1] in graph.keys()): graph[e[1]].append([int(e[2]),e[0]])
        else: graph[e[1]] = [[int(e[2]),e[0]]]
    # 각 노드에 연결되어 있지 않은 노드들은 비용을 'inf'로 설정하여 추가해준다.
    # keys = list(graph.keys())
    # for k in keys:
    #     tmp = [e[1] for e in graph[k]]
    #     diff = list((collections.Counter(keys) - collections.Counter(tmp)).keys())
    #     for d in diff:
    #         if(d==k): graph[k].append([0,d])
    #         else: graph[k].append([float('inf'),d])

    # for k in keys:
    #     graph[k] = sorted(graph[k],key=lambda x:x[1])
            
    return graph

def dijkstra(graph,src):
    INF = float('inf')
    V = sorted(list(graph.keys()))
    table = [[INF,src] if(v!=src) else [0,v] for v in V]
    visited = []
    queue = []
    heapq.heappush(queue,[0,src])
    while queue:
        tmp = heapq.heappop(queue)
        v = V[table.index(tmp)]
        if(v in visited): continue
        visited.append(v)
        for k in graph[v].keys():
            pos = V.index(k)
            table[pos] = [graph[v][k],tmp[1]] if(graph[v][k] < table[pos][0]) else table[pos]
            heapq.heappush(queue,table[pos])

    return table

def main():
    v, e = map(int, sys.stdin.readline().strip().split())
    src, dst = sys.stdin.readline().strip().split()
    edges = [sys.stdin.readline().strip().split() for _ in range(e)]
    graph = makeGraphDict(edges)
    for k in graph.keys():
        print(k + ' : ', end='')
        print(graph[k])
    result = dijkstra(graph,src)
    print(result)
    # print('  ',end='')
    # print(*vectors)
    # for i,n in enumerate(graph):
    #     print(vectors[i]+" ",end='')
    #     print(*n)
if __name__=='__main__':
    main()