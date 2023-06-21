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

def main():
    graph = {
        'A':['B','C'],
        'B':['A','D','E'],
        'C':['A','F'],
        'D':['B'],
        'E':['B','F'],
        'F':['C','E']
    }
    print(dfs(graph,'A'))

if __name__=='__main__':
    main()