import re
n = int(input())
def isClosed(s : str):
    while s:
        before = len(s)
        s = re.sub('\(\)|\[\]|\{\}','',s)
        after = len(s)
        if before==after:
            return 'NO'
    return 'YES'
for _ in range(n):
    s = input()
    print(isClosed(s))
