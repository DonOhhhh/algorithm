from copy import deepcopy

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if(parent[v] != v):
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)

    if root1 != root2:
        if(rank[root1] > rank[root2]):
            parent[root2] = root1
        else:
            parent[root1] = root2
            if(rank[root1] == rank[root2]):
                rank[root2] += 1 

def kruskal(vertex_list, edge_list):
    for u in vertex_list:
        make_set(u)
    
    edges = sorted(edge_list)
    mst = []
    sum = 0

    for e in edges:
        cost, u, v = e
        if(find(u) != find(v)):
            union(u, v)
            mst.append(e)
            sum += cost
    return sum, mst

def main():
    N,M = map(int,input().replace('\ufeff','').split())
    vertices = input().replace('\ufeff','').split()
    edges = []
    for _ in range(M):
        u, v, c = input().replace('\ufeff','').split()
        edges.append((int(c), u, v))

    # 모든 경로에서 임의의 1개의 경로를 삭제한 그래프의 최소 비용을 구한 후  
    # 두 번째로 작은 비용을 출력한다.
    result = []
    for i in range(len(edges)):
        tmp = deepcopy(edges)
        tmp.pop(i)
        mst = kruskal(vertices,tmp)[0]
        if(mst not in result):
            result.append(mst)
    print(sorted(result)[1])

if __name__=='__main__':
    main()