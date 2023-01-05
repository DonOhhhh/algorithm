from collections import deque
cards = list(range(1,int(input())+1))
while len(cards) != 1:
	tmp = deque(cards[1::2])
	if len(cards) % 2 == 1:
		tmp.append(tmp.popleft())
	cards = list(tmp)
print(cards[0])