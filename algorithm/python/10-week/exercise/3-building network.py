def buildingNetwork(n,cp,bp):
    base = [False for _ in range(n)] # 기지가 연결되었는지 확인하는 배열
    sum = 0 # 모든 경로의 비용을 담을 변수
    isolated = [] # 기지국을 건설할 노드들을 담을 배열
    connected = [] # 기지국들끼리 연결된 노드들을 담을 배열
    result = [] # 최소 비용 경로들을 담을 배열
    for c in cp:
        # 기지가 연결되었는지 확인하여 연결되지 않았다면 해당 기지가 연결되었다고 표시하고 그 경로의 비용을 더한다.
        if(not base[c[0]-1] or not base[c[1]-1]):
            base[c[0]-1] = True
            base[c[1]-1] = True
            sum += c[2]
            # 만약 두 값이 같다면 기지국 건설비용이므로 isolated에 담고
            if(c[0]==c[1]): isolated.append(c[0])
            # 두 값이 다르다면 노드 연결비용이므로 connected에 추가한다.
            else: connected.extend(c[0:2])
            # 최소 비용 간선으로 채택된 c를 result에 담는다.
            result.append(c)
    # 모든 노드의 기지국 건설비용 배열에서 connected에 있는 노드들에 해당하는 위치에 있는 비용을 edges에 저장한다.
    # 그와 동시에 connected에 존재하는 노드들이 isolated에 존재하는지 확인한다.
    # 만약 두 배열에 동시에 존재하는 노드가 1개라도 있다면 연결된 트리에 기지국이 존재한다는 의미이므로
    # isDone을 True로 만들어서 그 다음 코드가 실행되지 못하도록 한다.
    edges = []
    isDone = False
    for c in connected:
        if(c in isolated): isDone = True
        edges.append(bp[c-1])
    # 만약 isolated와 connected의 노드가 단 한개도 겹치지 않는다면
    # connected에 있는 노드들중 기지국을 건설한 노드가 한 개도 없다는 뜻이므로
    # edges에서 최소 비용을 가져오고 기지국 건설비용에서 해당 비용에 해당하는 노드를 찾은 뒤
    # 해당 노드의 경로와 비용을 result와 sum에 추가한다.
    if(not isDone):
        minEdge = min(edges)
        i = bp.index(minEdge)+1
        result.append([i,i,minEdge])
        sum += minEdge

    return sum, sorted(result,key=lambda x:x[2])

# 기지국 건설비용을 자기자신으로 가는 경로로 설정하여 edge를 원래 비용경로에 추가해준다.
def buildingConnectingMap(buildingPrice,connectingPrice):
    for i,b in enumerate(buildingPrice):
        connectingPrice.append([i+1,i+1,b])
    # 바뀐 비용경로를 비용 순으로 정렬하여 리턴한다.
    return sorted(connectingPrice,key=lambda x: [x[2],x[0],x[1]])

def main():
    nodeNum, edgeNum = map(int, input().replace('\ufeff','').split())
    buildingPrice = list(map(int,input().replace('\ufeff','').split()))
    connectingPrice = [list(map(int,input().replace('\ufeff','').split())) for _ in range(edgeNum)]
    
    newConnectingPrice = buildingConnectingMap(buildingPrice,connectingPrice)
    # print(newConnectingPrice)
    print(buildingNetwork(nodeNum,newConnectingPrice,buildingPrice))

if __name__=='__main__':
    main()