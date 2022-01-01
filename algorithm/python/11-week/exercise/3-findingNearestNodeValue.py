def nearestNode(node,target,k):
    tmp = []
    # target과 node들의 차를 tmp이 저장한다.
    for i in range(len(node)):
        tmp.append(abs(node[i]-target))
    # tmp를 정렬한 후 0부터 k-1까지의 값을 result에 저장한다.
    result = sorted(tmp)[0:k]
    # 정렬하기 전 tmp에서 각 값들의 위치를 찾아서 해당 위치에 해당하는 node들의 값을 nearest에 저장한다.
    nearest = []
    for i in result:
        nearest.append(node[tmp.index(i)])
    return nearest # nearest를 리턴해준다.

def main():
    n = int(input())
    node = list(map(int,input().split()))
    target = float(input())
    k = int(input())
    result = nearestNode(node,target,k)
    print(*result)

if __name__=='__main__':
    main()