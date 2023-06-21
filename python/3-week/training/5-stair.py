def stair(n):
    if n <= 1:
        return 1
    elif n == 2:
        return stair(1) + stair(0)
    else:
        return stair(n-1) + stair(n-2)

def stair_dp(n):
    if n<=1:
        return n
    dp = [int(0) for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def main():
    n = int(input().replace('\ufeff','').strip())
    print(stair(n))
    print(stair_dp(n))

if __name__=='__main__':
    main()