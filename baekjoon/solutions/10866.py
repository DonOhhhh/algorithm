from collections import deque
import sys


def input():
    return sys.stdin.readline().strip()


def print(x):
    sys.stdout.write(str(x) + "\n")


mem = deque()
n = int(input())
opSet = {
    "push_front" : lambda x,y : x.appendleft(y),
    "push_back" : lambda x,y : x.append(y),
    "pop_front" : lambda x : x.popleft(),
    "pop_back" : lambda x : x.pop(),
    "size": lambda x: len(x),
    "empty": lambda x: 0 if len(x) else 1,
    "front": lambda x: x[0],
    "back": lambda x: x[-1],
}
for _ in range(n):
    op = input()
    # print(op + ' ' + ' '.join(mem))
    try:
        print(opSet[op](mem))
    except IndexError:
        print(-1)
    except KeyError:
        op, arg = op.split()
        opSet[op](mem,arg)
