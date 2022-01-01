def makeTree(edges):
    tree = {}
    for e in edges:
        tree[e[0]] = []
        if(e[1]!='.'): tree[e[0]].append(e[1])
        else: tree[e[0]].append(None)
        if(e[2]!='.'): tree[e[0]].append(e[2])
        else: tree[e[0]].append(None)
    return tree

def printOrder(tree, root, visited, ordNum):
    if(root==None): return []
    if(ordNum==1): visited.append(root) # 1인 경우 preorder
    printOrder(tree,tree[root][0],visited, ordNum) # left
    if(ordNum==2): visited.append(root) # 2인 경우 inorder
    printOrder(tree,tree[root][1],visited, ordNum) # right
    if(ordNum==3): visited.append(root) # 3인 경우 postorder
    return visited

def main():
    n = int(input())
    edges = [input().split() for _ in range(n)]
    tree = makeTree(edges)
    for i in range(1,4):
        tmp = printOrder(tree,'A',[],i)
        print(''.join(tmp))

if __name__=='__main__':
    main()