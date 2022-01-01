def commonArea(country,towns,trg1, trg2):
    a,b = '',''
    # town에서 target1과 target2의 도시를 찾는다.
    for town in towns.keys():
        if(trg1 in towns[town]):
            a = town
        if(trg2 in towns[town]):
            b = town
    if(trg1==trg2): return trg1 # 만약 구 이름이 같다면 그냥 구 이름을 리턴해준다.
    if(a=='' or b==''): return 0 # 만약 둘 중 하나라도 못찾았다면 0을 리턴해준다.
    if(a==b): return a # 만약 찾은 값이 같다면 해당 시의 이름을 돌려준다.
    if(a!=b): return country # 둘 다 찾았지만 값이 다른 경우 country를 리턴해준다.

def main():
    n = int(input())
    trg1, trg2 = input().split()
    tmp = input().split()
    country = tmp[0]
    tmp = [input().split() for _ in range(n-1)]
    town = {}
    for t in tmp:
        town[t[0]] = t[1:]
    # print(country)
    # print(city)
    # print(town)
    result = commonArea(country,town,trg1,trg2)
    print(result)
   
if __name__=='__main__':
    main()