def coin_change(coinList, goal_cash,cnt):
    if goal_cash<=1: return 1
    else:
        for i in coinList:
            if goal_cash >= i:
                return coin_change(coinList,goal_cash-i,cnt) + 1

if __name__=='__main__':
    coinList = list(map(int,input().replace('\ufeff','').split()))
    goal_cash = int(input().replace('\ufeff',''))
    print(coin_change(list(reversed(coinList)), goal_cash,0))