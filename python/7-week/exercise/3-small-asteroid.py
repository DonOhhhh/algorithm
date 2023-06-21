#201904014 Dong Joon Oh
import bisect
import heapq

def removeAsteroid(weights):
    weights.sort() # 무게 배열을 정렬함.
    while(not(len(weights)<=1)): # 무게 배열의 길이가 1보다 작을 때까지 동작함.
        a,b = weights.pop(-1),weights.pop(-1) # 제일 무거운 무게 2개를 배열에서 빼내옴.
        if(a-b!=0): # 만약 두 무게가 같지 않다면 배열의 적절한 위치에 두 값의 차를 넣어줌. 두 무게가 같다면 그냥 넘어감.
            weights.insert(bisect.bisect(weights,a-b),a-b) 
    return weights[0] if(len(weights)!=0) else 0 # 배열이 없으면 0을 있다면 마지막 남은 값 1개를 리턴함.

def removeAsteroidUsingMaxHeap(weights):
    newArr = [] # 최대 힙을 구성할 배열
    # 최대 힙 구성
    for w in weights:
        heapq.heappush(newArr,(-w,w))
    
    while(not(len(newArr) <= 1)):
        # 최대 힙에서 제일 큰 두 값을 뺌
        a,b = heapq.heappop(newArr)[1], heapq.heappop(newArr)[1]
        # 만약 두 값의 차가 0이 아니라면 두 값의 차를 heap에 넣어줌. 0이라면 넘어감
        if(a-b!=0):
            heapq.heappush(newArr, (-(a-b),a-b))
    # 만약 newArr의 길이가 1이라면 힙의 제일 마지막 값을 리턴하고 아니라면 0을 리턴
    return heapq.heappop(newArr)[1] if(len(newArr) == 1) else 0

def main():
    Asteroid_weights = list(map(int,input().replace('\ufeff','').strip().split()))
    # print(removeAsteroid(Asteroid_weights))
    print(removeAsteroidUsingMaxHeap(Asteroid_weights))

if __name__=='__main__':
    main()