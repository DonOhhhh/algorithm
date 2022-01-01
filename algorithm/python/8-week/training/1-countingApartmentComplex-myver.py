def dfs(graph,root):
    visit = []
    stack = [root]
    while stack:
        tmp = stack.pop()
        if(tmp not in visit):
            visit.append(tmp)
            stack.extend(graph[tmp])
    return visit

def cac2(n,complex):
    # 1이 있는 배열의 위치를 저장함.
    unsortedComplexes = [[i,j] if(complex[i][j]==1) else None for j in range(n) for i in range(n)]
    unsortedComplexes = sorted(list(filter(lambda x: x!=None, unsortedComplexes)))
    # 1이 있는 위치와 연결된 위치들을 dict형태로 저장함.
    graph = dict()
    for i,c1 in enumerate(unsortedComplexes):
        tmp=[]
        for c2 in unsortedComplexes:
            if([c1[0],c1[1]-1]==c2):
                tmp.append(c2)
            if([c1[0],c1[1]+1]==c2):
                tmp.append(c2)
            if([c1[0]-1,c1[1]]==c2):
                tmp.append(c2)
            if([c1[0]+1,c1[1]]==c2):
                tmp.append(c2)
        graph[i] = tmp
    # dict형태로 저장된 값들을 정수형태로 바꿔서 dict로 저장함.
    graph2 = dict()
    for i in range(len(unsortedComplexes)):
        graph2[i] = []
        for j in graph.keys():
            if(i==j): continue
            if(unsortedComplexes[i] in graph[j]):
                graph2[i].append(j)
    # 정수형태로 저장된 그래프를 dfs를 통하여 어떤 그래프들 끼리 연결되어 있는지 파악함.
    result = []
    while graph2:
        tmp = dfs(graph2,list(graph2.keys())[0])
        result.append(len(tmp))
        for i in tmp:
            graph2.pop(i)
    # 배열의 길이와 result를 리턴함.
    return [len(result)] + sorted(result)

def main():
    n = int(input().replace('\ufeff',''))
    complex = [list(map(int, input().replace('\ufeff',''))) for _ in range(n)]
    for i in cac2(n,complex): print(i)

if __name__=='__main__':
    main()