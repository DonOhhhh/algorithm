from collections import Counter

n = int(input())
cards = Counter(list(map(int,input().split())))
m = int(input())
nums = list(map(int,input().split()))
for n in nums:
    print(cards[n],end=' ')
print()
