import sys

n = int(input().replace('\ufeff','').strip())
total_sum = 0

for line in sys.stdin.readlines():
    total_sum += sum([int(i) for i in line.split()])
print(total_sum)