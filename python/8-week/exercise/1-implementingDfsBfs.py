#201904014 Dong Joon Oh

# bfs는 큐를 이용하여 탐색한다.
def bfs(graph,root):
    visit = []
    queue = []
    queue.append(root)
    while queue:
        tmp = queue.pop(0)
        if(tmp not in visit):
            visit.append(tmp)
            queue.extend(graph[tmp])
    return visit

# dfs는 스택을 이용하여 탐색한다.
def dfs(graph,root):
    visit=[]
    stack=[]
    stack.append(root)
    while stack:
        tmp = stack.pop()
        if(tmp not in visit):
            visit.append(tmp)
            stack.extend(graph[tmp])
    return visit

def main():
    root = input()
    dic = dict()
    for i in range(13):
        tmp = input().split()
        dic[tmp[0]] = tmp[1:]
    print(*bfs(dic,root))
    print(*dfs(dic,root))

if __name__=='__main__':
    main()
