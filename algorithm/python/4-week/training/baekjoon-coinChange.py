def coin_change_dp(coinList, goal_cash, cnt):
    for i in coinList:
        cnt += goal_cash // i
        goal_cash %= i
    return cnt

def coin_change(coinList, goal_cash,cnt):
    if goal_cash==0: return 0
    else:
        for i in coinList:
            if goal_cash >= i:
                return coin_change(coinList,goal_cash-i,cnt) + 1

if __name__=='__main__':
    n,k = map(int,input().replace('\ufeff','').split())
    coinList = [int(input().replace('\ufeff','')) for i in range(n)]
    print(coin_change_dp(list(reversed(coinList)), k,0))