import bisect
n = int(input())
prison = list(map(int,input().split()))
m = int(input())
ligther = sorted(list(map(int,input().split())))
supplyStatsus = {}
for p in prison:
    x = bisect.bisect(ligther,p)
    if x==0:
        supplyStatsus[p] = abs(ligther[x]-p)
    elif x==len(ligther):
        supplyStatsus[p] = abs(ligther[x-1]-p)
    else:
        supplyStatsus[p] = abs(ligther[x-1]-p) if abs(ligther[x-1]-p) < abs(ligther[x]-p) else abs(ligther[x]-p)
result = 0
for p in prison:
    result = supplyStatsus[p] if supplyStatsus[p] > result else result
print(result)
