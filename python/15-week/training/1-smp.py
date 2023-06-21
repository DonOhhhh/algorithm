def smp(n,male,female,gender):
    people = {i+1 : None for i in range(n)}
    chosen = []
    wait_gender, dash_gender = None, None
    # 남자 기준
    if(gender=='male'):
        wait_gender, dash_gender = male, female
    # 여자 기준
    elif(gender=='female'):
        wait_gender, dash_gender = female, male

    for i in range(n):
        if(len(chosen)==n): break # baekjoon 12022 / 모든 짝들이 서로 선호도가 제일 높은 짝과 결합했다면 탈출
        pref = [dash_gender[j][i] for j in range(n)]
        for h,f in enumerate(pref):
            if(len(chosen)==n): break # baekjoon 12022 / 모든 짝들이 서로 선호도가 제일 높은 짝과 결합했다면 탈출
            if(h+1 in chosen): continue
            if(people[f] == None):
                people[f] = h+1
            elif(wait_gender[f-1].index(h+1) < wait_gender[f-1].index(people[f])):
                chosen.remove(people[f])
                people[f] = h+1
            else:
                continue
            chosen.append(people[f])
    return list(people.values())

def main():
    n = int(input())
    malePref = [list(map(int,input().split())) for _ in range(n)]
    femalePref = [list(map(int,input().split())) for _ in range(n)]
    print(smp(n,malePref,femalePref,'male'))

if __name__=="__main__":
    main()