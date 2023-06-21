def stair(n,m):
    if n <= 1: return 1
    else:
        way = 0
        for i in range(1,m+1):
            if i > n: break
            way += stair(n-i,m)
    return way

def stair_dp(n,m):
    if n<=1:
        return n
    dp = [int(0) for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        for j in range(1,m+1):
            dp[i] += dp[i-j]
    return dp[n]      

if __name__=='__main__':
    n,m = map(int,input().replace('\ufeff','').split())
    print(stair(n,m))
    print(stair_dp(n,m))