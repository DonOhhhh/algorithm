from copy import deepcopy

def dfs(graph,root):
    visit = []
    stack = [root]
    while stack:
        tmp = stack.pop()
        if(tmp not in visit):
            visit.append(tmp)
            stack.extend(graph[tmp])
    return visit

def main():
    n,m = map(int,input().replace('\ufeff','').split())
    stations = input().replace('\ufeff','').split()
    route = [input().replace('\ufeff','').split() for i in range(m)]
    graph = dict()
    # 각 역에 연결되어 있는 역들을 딕셔너리로 만든다.
    for s in stations:
        graph[s] = []
        # 간선의 시작점과 끝점에서 s와 같은 역이 있는지 검사한다.
        for r in route:
            if(s in r):
                # 만약 있다면 해당 route 배열을 카피한다.
                # 카피한 tmp배열에서 역 s를 삭제한다.
                tmp = deepcopy(r)
                tmp.remove(s)
                # tmp의 나머지 요소들을 돌면서 graph[s]에 해당 역이 있는지 검사하여 없다면 추가한다.
                for i in tmp:
                    if(i not in graph[s]):
                        graph[s].append(i)
    # 딕셔너리로 만든 각 역에 연결표를 dfs로 순회한 후 순회한 결과의 길이가 역의 전체 개수와 같다면 True를 다르다면 False를 리턴한다.
    result = True if(len(dfs(graph,list(graph.keys())[0])) == len(stations)) else False
    print(result)

if __name__=='__main__':
    main()