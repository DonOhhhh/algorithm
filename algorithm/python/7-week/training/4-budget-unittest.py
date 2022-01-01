import unittest

def getUpperLimit2(budgets,m):
    if(sum(budgets) <= m): return max(budgets)
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

def getUpperLimit(budgets,m):
    if(sum(budgets) <= m): return max(budgets)
    # 순차 검색
    # listOfRange = [x for x in range(min(budgets),max(budgets)+1)]
    # cnt = 0
    # while cnt < len(listOfRange):
    #     tmp = [listOfRange[cnt] if(x>listOfRange[cnt]) else x for x in budgets]
    #     if(sum(tmp) > m): return listOfRange[cnt-1]
    #     cnt += 1
    
    # 이진 검색
    # 필요 예산을 0에서부터 최대값사이에서 이진 검색을 하면서 start와 end의 범위가 2가 될 때까지 탐색함.
    start = 0
    end = max(budgets)
    middle = (end-start)//2

    while(end-start!=2):
        budgetSum = [middle if(x>middle) else x for x in budgets]
        diff = sum(budgetSum) - m
        if(diff > 0):
            end = middle
            middle = end - (end-start)//2
        elif(diff < 0):
            start = middle
            middle = start + (end-start)//2
        else:
            break

    # 만약 함계가 전체 예산보다 크다면 -1을 하여 리턴하고 아니면 그냥 middle을 리턴함.
    diff = sum([middle if(x>middle) else x for x in budgets]) - m
    return middle-1 if(diff > 0) else middle

# TestCase를 작성
class CustomTests(unittest.TestCase): 

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.inOutPut = {
            127 : ['120 110 140 150',485],
            100 : ['70 80 30 40 100',450],
            6 : ['10 20',12],
            1 : ['4 4 5 5 2',7],
            1 : ['3 2 4',5],
            2 : ['4 4 5', 6],
            6 : ['10 20',12],
            100 : ['101 101 101 101', 400],
            4 : ['4 3 2 1', 10],
            4 : ['10 1', 5],
            497 : ['384 387 278 416 294 336 387 493 150 422 363 28 191 60 264 427 41 427 173 237 212 369 68 430 283 31 363 124 68 136 430 303 23 59 70 168 394 457 12 43 230 374 422 420 285 38 199 325 316 371 414 27 92 481 457 374 363 171 497 282 306 426 85 328 337 6 347 230 314 358 125 396 83 46 315 368 435 365 44 251 88 309 277 179 289 85 404 152 255 400 433 61 177 369 240 13 227 87 95 40', 50000],
            61 : ['110 150 74 112 54 144 56 112', 480],
            20 : ['77 89 61 118 91 142',120]
        }

    def test_runs(self):
        for i in self.inOutPut.keys():
            self.assertEqual(i,getUpperLimit2(list(map(int,self.inOutPut[i][0].split())),self.inOutPut[i][1]))
    

# unittest를 실행
if __name__ == '__main__':  
    unittest.main()