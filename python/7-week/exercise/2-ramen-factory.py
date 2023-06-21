#201904014 Dong Joon Oh
import heapq

def factory(stock, dates, supplies, k):
    import_count = 0
    stock_heap =[]
    index = 0

    # 재고가 다 떨어질 때까지 동작한다.
    while(stock < k):
        # 모든 공급받을 수 있는 날짜 중 stock보다 작거나 같은 날짜를 최대 heap에 넣는다.
        for i in range(index, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(stock_heap, (-supplies[i], supplies[i]))
                index = i+1
            else:
                break
        # 최대 힙에서 가장 큰 값을 빼서 stock에 더하고 import_count를 1증가시킨다.
        max_amount = heapq.heappop(stock_heap)[1]
        stock += max_amount
        import_count += 1
    return import_count

def main():
    stock, k, n, m = map(int,input().replace('\ufeff','').strip().split())
    dates = list(map(int, input().replace('\ufeff','').split()))
    supplies = list(map(int, input().replace('\ufeff','').split()))

    print(factory(stock,dates, supplies, k))
if __name__=='__main__':
    main()