import sys

def makeTree(edges):
    result = {}
    for e in edges:
        if(e[0] in result.keys()):
            result[e[0]].append(e[1])
        elif(e[1] in result.keys()):
            result[e[1]].append(e[0])
        else:
            result[e[0]] = [e[1]]
            
    return result

def dfs(tree,root,nodes=[],depth=[0]):
    nodes.append(root)
    depth.append(depth[-1]+1)
    if(root not in list(tree.keys())): return
    for i in tree[root]:
        dfs(tree,i,nodes,depth)
        nodes.append(root)
        depth.append(depth[-1]-1)
    return nodes, depth

def getMinIndex(arr):
    # result = [0,float('inf')]
    # for i,num in enumerate(arr):
    #     result = [i,num] if(num < result[1]) else result
    # return result[0]
    return arr.index(min(arr))

def main():
    n = int(input())
    edges = [list(map(int,input().split())) for _ in range(n-1)]
    m = int(input())
    search_nodes = [list(map(int,input().split())) for _ in range(m)]

    tree = makeTree(edges)
    nodes, depth = dfs(tree,1)
    depth.pop(0)
    
    print(tree)
    print(nodes)
    print(depth)
    
    for n in search_nodes:
        targetA = min(nodes.index(n[0]), nodes.index(n[1]))
        targetB = max(nodes.index(n[0]), nodes.index(n[1]))+1
        i = getMinIndex(depth[targetA:targetB])
        print(nodes[targetA:targetB][i])

if __name__=='__main__':
    main()