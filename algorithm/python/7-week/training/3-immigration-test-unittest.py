import unittest
# 이진 검색
def immigrationTest(m,times):
    start = 1
    end = max(times)*m
    result = 0
    
    while(end>=start):
        mid = (end+start)//2
        if(sum([mid//i for i in times]) < m):
            start = mid+1
        else:
            end = mid-1
            result = mid

    return result

# TestCase를 작성
class CustomTests(unittest.TestCase): 

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.inOutPut = {
            1000000000000000000 : [1,1000000000,'1000000000'],
            1 : [2,1,'1 1'],
            4 : [18,6,'6 2 21 19 4 27 7 18 5 1 14 29 21 12 13 19 8 17'],
            8 : [10,8,'7 3 16 5 18 2 13 12 10 17'],
            12 : [12, 13, '8 27 6 3 10 5 11 14 21 19 12 8'],
            50000000 : [20, 1000000000, '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'],
            27105055 : [41, 1000000000, '666916 752 17 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'],
            54210109 : [22, 1000000000, '1282561 435 9 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'],    
            125000001 : [13, 1000000000, '3258830 1807 43 7 3 2 1 1 1 1 1 1 1'],
            250000001 : [9, 1000000000, '3261135 1807 43 7 3 2 1 1 1'],
            125000000 : [8, 1000000000, '1 1 1 1 1 1 1 1']
        }

    def test_runs(self):
        for i in self.inOutPut.keys():
            self.assertEqual(i,immigrationTest(self.inOutPut.get(i)[1],list(map(int,self.inOutPut.get(i)[2].split(' ')))))
    

# unittest를 실행
if __name__ == '__main__':  
    unittest.main()