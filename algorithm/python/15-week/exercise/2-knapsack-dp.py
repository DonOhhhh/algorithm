def knapsack(capacity, n, weights, values):
    array = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for s in range(1, capacity+1):
            if(weights[i-1] > s):
                array[i][s] = array[i-1][s]
            else:
                array[i][s] = max(values[i-1] + array[i-1][s-weights[i-1]], array[i-1][s])
    return array[n][capacity]

def main():
    max_weight = int(input())
    n = int(input())
    weights = list(map(int,input().split()))
    values = list(map(int,input().split()))
    print(knapsack(max_weight,n,weights,values))

if __name__=='__main__':
    main()