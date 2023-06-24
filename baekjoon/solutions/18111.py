import sys

def isPossible(b, ground, start, end):
    curHeight = (end + start) // 2
    availBlocks = list(map(lambda x: x - curHeight, ground))
    if sum(availBlocks) + b < 0:
        # return float('inf'), 0
        return getLeastTime(b, ground, float("inf"), 0, start, curHeight-1)
    else:
        workingTime = sum(list(map(lambda x: x * 2 if x > 0 else abs(x), availBlocks)))
        return workingTime, curHeight


def getLeastTime(b, ground, minTime, maxHeight, start, end):
    mid = (end + start) // 2
    if end < start:
        return minTime, maxHeight
    leftTime, leftHeight = isPossible(b, ground, start, mid - 1)
    rightTime, rightHeight = isPossible(b, ground, mid + 1, end)
    print(f"{start} {mid} {end} {leftTime, leftHeight} {rightTime, rightHeight}\n")
    if leftTime < rightTime:
        tmpTime, tmpHeight = getLeastTime(
            b, ground, leftTime, leftHeight, start, mid - 1
        )
    elif rightTime < leftTime:
        tmpTime, tmpHeight = getLeastTime(
            b, ground, rightTime, rightHeight, mid + 1, end
        )
    else:
        if rightTime != float('inf'):
            tmpTime, tmpHeight = min(
                [
                    getLeastTime(b, ground, leftTime, leftHeight, start, mid - 1),
                    getLeastTime(b, ground, rightTime, rightHeight, mid + 1, end)
                ],
                key=lambda x: (x[0], -x[1]),
            )
        else:
            return minTime, maxHeight
    if tmpTime < minTime:
        return tmpTime, tmpHeight
    else:
        if tmpTime == minTime and tmpHeight > maxHeight:
            maxHeight = tmpHeight
        return minTime, maxHeight


input = sys.stdin.readline
print = sys.stdout.write

n, m, b = map(int, input().split())
ground = " ".join((input() for _ in range(n)))
ground = list(map(int, ground.split()))
start, end = min(ground), max(ground)
time, height = isPossible(b, ground, start, end)
t, h = getLeastTime(b, ground, time, height, start, end)
print(f"{t} {h}")
