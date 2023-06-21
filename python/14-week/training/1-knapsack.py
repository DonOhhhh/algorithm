import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline
branch = []

def knapsack_bruteForce(n,limit,weight_value):
    maxValue = -float('inf')
    wv = {}
    for w,v in weight_value:
        if(w not in wv.keys()):
            wv[w] = [v]
        else:
            wv[w].append(v)
    
    weight = [weight_value[i][0] for i in range(n)]
    for i in range(1,n+1):
        for c in combinations(weight,i):
            if(sum(list(c)) > limit): continue
            total = []
            for i,k in enumerate(c):
                if(wv[k][i] not in total):
                    total.append(wv[k][i])
            if(sum(total) > maxValue): maxValue = sum(total)

    return maxValue

def knapsack_recursion(n,limit,value,w_v,maxValue,mem=[]):
    for w,v in w_v:
        if(w > limit): continue
        tmp = deepcopy(w_v)
        tmp.remove([w,v])
        total = knapsack_recursion(n,limit-w,value+v,tmp,maxValue,mem)
        if(total > maxValue): maxValue = total
    return maxValue if(maxValue > value) else value

def knapsack_dp_memoization(n,limit,value,w_v,maxValue):
    return

def main():
    n, w = map(int,input().strip().split())
    weight_value = [list(map(int,input().strip().split())) for _ in range(n)]
    print(knapsack_recursion(n,w,0,weight_value,-float('inf'),[]))
    print(knapsack_bruteForce(n,w,weight_value))

if __name__=='__main__':
    main()