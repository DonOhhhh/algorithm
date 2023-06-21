#201904014 Dong Joon Oh
from copy import deepcopy

# dfs
def dfs(graph,root):
    visit = []
    stack = []
    stack.append(root)
    while stack:
        tmp = stack.pop()
        if(tmp not in visit):
            visit.append(tmp)
            stack.extend(graph[tmp])
    return visit

# 무역로에서 경로를 한 개씩 삭제한 다음 dfs를 이용하여 도달 가능한 무역로의 개수를 체크한다.
# 해당 무역로의 개수가 n과 같지 않다면 해당 경로는 독점 무역로로 판정한다.
def tradingRoute(n,m,routes,graph):
    result = []
    for i in routes:
        tmp = deepcopy(graph)
        tmp[i[0]].remove(i[1])
        tmp[i[1]].remove(i[0])

        splited = dfs(tmp,0)
        # print(splited)
        if(len(splited) != n): result.append(sorted(i))
    return sorted(result,key=lambda x:x[0])

def main():
    n,m = map(int,input().replace('\ufeff','').strip().split())
    routes = [list(map(int,input().replace('\ufeff','').strip().split())) for i in range(m)]

    # 전달받은 경로들로 부터 그래프를 만든다.
    graph = dict()
    for i in range(n): graph[i] = []     

    for i in range(n):
        tmp = deepcopy(routes)
        for j in range(len(tmp)):
            if(i in tmp[j]):
                tmp[j].remove(i)
                graph[i] += tmp[j]
    result = tradingRoute(n,m,routes,graph)
    for i in result: print(*i)

if __name__=='__main__':
    main()