import sys

count = int(input().replace('\ufeff','').strip())
sum = 0

for line in sys.stdin.readlines():
    sum += int(line)

print(sum)