n = int(input())
stack = []
result = []
cnt = 1
for _ in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        cnt += 1
        result.append("+")
    if num == stack[-1]:
        result.append("-")
        stack.pop()

if stack:
    print("NO")
else:
    print("\n".join(result))