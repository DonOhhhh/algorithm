import sys
import heapq

def makeGraph(edges):
    graph = {}
    
    for e in edges:
        if(e[0] in graph.keys()): graph[e[0]][e[1]] = int(e[2])
        else: graph[e[0]] = {e[1]:int(e[2])}
        if(e[1] in graph.keys()): graph[e[1]][e[0]] = int(e[2])
        else: graph[e[1]] = {e[0]:int(e[2])}
    return graph

def dijkstra(graph, start, end):
    # start로 부터의 거리 값을 저장하기 위함
    distances = {node: [float('inf'), start] for node in graph}  
    distances[start] = [0, start]  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start][0], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        # 탐색 할 노드, 거리를 가져옴.
        current_distance, current_destination = heapq.heappop(queue)

        # 기존에 있는 거리보다 길다면, 볼 필요도 없음
        if distances[current_destination][0] < current_distance: continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination][0]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = [distance, current_destination]
                # 다음 인접 거리를 계산 하기 위해 큐에 삽입
                heapq.heappush(queue, [distance, new_destination])
    tmp = end
    path = end
    while distances[tmp][1]!=start:
        tmp = distances[tmp][1]
        path = tmp + path
        
    return start + path, distances[end][0]

def main():
    v, e = map(int, sys.stdin.readline().strip().split())
    src, dst = sys.stdin.readline().strip().split()
    vertices = sys.stdin.readline().strip().split()
    edges = [sys.stdin.readline().strip().split() for _ in range(e)]
    graph = makeGraph(edges)
    # for k in graph.keys():
    #     print(k + ' : ', end='')
    #     print(graph[k])
    path, d = dijkstra(graph,src,dst)
    print(path)
    print(d)
if __name__=='__main__':
    main()