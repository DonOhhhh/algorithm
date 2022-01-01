
def BFS(graph,root):
    queue = []
    visit = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
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
    print(BFS(graph,'C'))

if __name__=='__main__':
    main()