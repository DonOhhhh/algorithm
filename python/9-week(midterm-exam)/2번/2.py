import bisect
def power_supply(base,power_station):
    # 전력 공급 상태를 담을 딕셔너리를 만든다.
    supplyStatus = {}
    # 각 기지를 기준으로 연결되어 있는 전력 공급소를 찾는다.
    for b in base:
        # 이분 탐색으로 전력소배열에서 기지의 위치를 찾는다.
        x = bisect.bisect(power_station,b)
        # x가 0이라면 기지가 전력소보다 작은 위치에 존재한다면 첫 번째 전력소의 위치와 그 전력소까지의 거리를 저장한다.
        if(x==0):
            supplyStatus[b] = [power_station[x],abs(power_station[x]-b)]
        # x가 전력소 배열의 크기와 같다면 기지가 전력소보다 큰 위치에 존재한다면 제일 마지막 전력소의 위치와 그 전력소까지의 거리를 저장한다.
        elif(x==len(power_station)):
            supplyStatus[b] = [power_station[x-1],abs(power_station[x-1]-b)]
        # 기지가 전력소 중간에 존재한다면 왼쪽가 오른쪽 전력소 중 더 가까운 곳과 거리를 저장한다.
        else:
            supplyStatus[b] = [power_station[x-1],abs(power_station[x-1]-b)] if(abs(power_station[x-1]-b) < abs(power_station[x]-b)) else [power_station[x],abs(power_station[x]-b)]
    # 찾은 딕셔너리에서 거리를 기준으로 가장 큰 값을 result에 저장 후 리턴한다.
    result = 0
    for k in supplyStatus.keys():
        result = supplyStatus[k][1] if(supplyStatus[k][1] > result) else result

    return result

def main():
    base = list(map(int,input().replace('\ufeff','').strip().split()))
    power_station = list(map(int,input().replace('\ufeff','').strip().split()))
    base.sort()
    power_station.sort()
    print(power_supply(base,power_station))
    
if __name__=='__main__':
    main()