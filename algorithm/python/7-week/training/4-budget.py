def getUpperLimit(budgets,m):
    # 예산의 합이 m보다 작거나 같다면 해당 예산의 최댓값이 예산의 limit이 된다.
    if(sum(budgets) <= m): return max(budgets)
    # 순차 검색
    # listOfRange = [x for x in range(min(budgets),max(budgets)+1)]
    # cnt = 0
    # while cnt < len(listOfRange):
    #     tmp = [listOfRange[cnt] if(x>listOfRange[cnt]) else x for x in budgets]
    #     if(sum(tmp) > m): return listOfRange[cnt-1]
    #     cnt += 1
    
    # 이진 검색 1
    # start = 0
    # end = max(budgets)
    # middle = (end+start)//2

    # while(end-start!=2):
    #     budgetSum = [middle if(x>middle) else x for x in budgets]
    #     diff = sum(budgetSum) - m
    #     if(diff > 0):
    #         end = middle
    #         middle = end - (end-start)//2
    #     elif(diff < 0):
    #         start = middle
    #         middle = start + (end-start)//2
    #     else:
    #         break

    # diff = sum([middle if(x>middle) else x for x in budgets]) - m
    # return middle-1 if(diff > 0) else middle

    start = 0
    end = max(budgets)
    result = 0

    while(end>=start):
        mid = (end+start)//2
        if(sum([mid if(x>mid) else x for x in budgets]) > m):
            end = mid-1  
        else: 
            start = mid+1
            result = mid
    return result
            
def main():
    n = int(input().replace('\ufeff',''))
    budgets = list(map(int, input().replace('\ufeff','').split()))
    m = int(input().replace('\ufeff',''))
    print(getUpperLimit(budgets,m))

if __name__ == '__main__':
    main()