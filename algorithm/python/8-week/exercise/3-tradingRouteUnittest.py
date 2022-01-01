import unittest
from copy import deepcopy

# TestCase를 작성
class CustomTests(unittest.TestCase): 

    def __init__(self, methodName: str = ...) -> None:
        # self.getAnswer = __import__('3-tradingRoute')
        super().__init__(methodName=methodName)
        self.inPut = [
            [[6, 7], [0, 1], [1, 3], [0, 2], [1, 2], [4, 5], [3, 4], [3, 5]],
            [[6, 6], [0, 1], [1, 3], [1, 2], [0, 2], [3, 4], [4, 5]],
            [[8, 8], [0, 1], [1, 4], [0, 2], [2, 3], [3, 7], [3, 6], [6, 7], [2, 5]],
            [[13, 16], [0, 1], [1, 6], [6, 10], [6, 7], [7, 10], [10, 11], [7, 8], [7, 11], [8, 11], [3, 7], [2, 4], [3, 4], [3, 5], [4, 5], [5, 9], [9, 12]],
            [[12, 14], [0, 2], [2, 4], [2, 3], [4, 5], [3, 5], [1, 3], [1, 6], [6, 9], [9, 10], [3, 7], [7, 10], [7, 8], [8, 11], [10, 11]]
        ]
        self.outPut = [
            [[1, 3]],
            [[1, 3], [3, 4], [4, 5]],
            [[0, 1], [0, 2], [1, 4], [2, 3], [2, 5]],
            [[0, 1], [1, 6], [2, 4], [3, 7], [5, 9], [9, 12]],
            [[0, 2]]
        ]

    def test_runs(self):
        for i,out in enumerate(self.outPut):
            self.assertEqual(out,self.takeValues(self.inPut[i][0][0],self.inPut[i][0][1],self.inPut[i][1:]))

    # dfs
    def dfs(self,graph,root):
        visit = []
        stack = []
        stack.append(root)
        while stack:
            tmp = stack.pop()
            if(tmp not in visit):
                visit.append(tmp)
                stack.extend(graph[tmp])
        return visit

    # 무역로에서 경로를 한 개씩 삭제한 다음 dfs를 이용하여 도달 가능한 무역로의 개수를 체크한다.
    # 해당 무역로의 개수가 n과 같지 않다면 해당 경로는 독점 무역로로 판정한다.
    def tradingRoute(self,n,m,routes,graph):
        result = []
        for i in routes:
            tmp = deepcopy(graph)
            tmp[i[0]].remove(i[1])
            tmp[i[1]].remove(i[0])

            splited = self.dfs(tmp,0)
            # print(splited)
            if(len(splited) != n): result.append(sorted(i))
        return sorted(result,key=lambda x:x[0])

    def takeValues(self,n,m,routes):
        # n,m = map(int,input().replace('\ufeff','').strip().split())
        # routes = [list(map(int,input().replace('\ufeff','').strip().split())) for i in range(m)]

        # 전달받은 경로들로 부터 그래프를 만든다.
        graph = dict()
        for i in range(n): graph[i] = []     

        for i in range(n):
            tmp = deepcopy(routes)
            for j in range(len(tmp)):
                if(i in tmp[j]):
                    tmp[j].remove(i)
                    graph[i] += tmp[j]
        result = self.tradingRoute(n,m,routes,graph)
        return result

# unittest를 실행
if __name__ == '__main__':  
    unittest.main()