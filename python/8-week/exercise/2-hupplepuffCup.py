#201904014 Dong Joon Oh
def hupplePuffsCup(graph,root):
	visit = []
	stack = []
	stack.append(root)
	while stack:
		tmp = stack.pop()
		if(tmp not in visit):
			visit.append(tmp)
			stack.extend(graph[tmp])
	return visit

def main():
	n = int(input())
	dic = dict()
    # 각 컵별로 답겨있는 쪽지를 리스트로 넣는다.
	for i in range(n):
		dic[i] = list(map(int,input().split()))

    # dfs를 통해 도달 가능한 컵들의 리스트를 만든 뒤 제일 마지막 값이 n-1과 같다면 true 아니면 false를 출력한다.
	print(True) if(sorted(hupplePuffsCup(dic,0))[-1]==n-1) else print(False)

if __name__=='__main__':
	main()