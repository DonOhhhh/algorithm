n = int(input())
for _ in range(n):
	ps = input()
	while ps.find('()') != -1:
		ps = ps.replace('()','')
	if ps:
		print('NO')
	else:
		print('YES')