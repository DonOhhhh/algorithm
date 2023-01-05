import sys


def input():
    return sys.stdin.readline().strip()


def print(x):
    sys.stdout.write(str(x) + "\n")


mem = list()
n = int(input())
opSet = {
    "size": lambda x: len(x),
    "empty": lambda x: 0 if len(x) else 1,
    "pop": lambda x: x.pop(0),
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
        mem.append(arg)
