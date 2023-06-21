import heapq

def dijkstra(edges, V, E, src, dst):
    INF = float('inf')
    distance = [INF for _ in range(V+1)]
    distance[src] = 0
    queue = []
    found = [False for _ in range(V + 1)]

    heapq.heappush(queue, [0, src])

    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True # found shortest path for v[1]
        for node_weight in edges[v[1]]:
            if(found[node_weight[0]]): continue
            if(distance[node_weight[0]] > distance[v[1]] + node_weight[1]):
                distance[node_weight[0]] = distance[v[1]] + node_weight[1]
                heapq.heappush(queue, [distance[node_weight[0]], node_weight[0]])
    return distance[dst]

def main():
    V, E = map(int, input().split())
    src, dst = map(int, input().split())
    edges = [ [] for _ in range(V+1)]

    for _ in range(E):
        i,j,c = map(int, input().split())
        edges[i].append([j,c])
    print(dijkstra(edges, V, E, src, dst))

if __name__=='__main__':
    main()