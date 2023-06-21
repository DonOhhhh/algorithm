import heapq

def factory(stock, dates, supplies, k):
    import_count = 0
    stock_heap =[]
    index = 0

    while(stock < k):
        for i in range(index, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(stock_heap, (-supplies[i], supplies[i]))
                index = i+1
            else:
                break
        max_amount = heapq.heappop(stock_heap)[1]
        stock += max_amount
        import_count += 1
    return import_count

def main():
    stock = int(input().replace('\ufeff',''))
    dates = list(map(int, input().replace('\ufeff','').split()))
    supplies = list(map(int, input().replace('\ufeff','').split()))
    k = int(input().replace('\ufeff',''))

    print(factory(stock,dates, supplies, k))
if __name__=='__main__':
    main()