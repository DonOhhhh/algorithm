def main():
    n = int(input())
    cnt = 0
    for i in range(1,n+1):
        s = reversed(list(map(int,str(i))))
        tmp = ''.join([str(x) for x in s])
        rStr = list(map(int,tmp))
        for j in range(len(rStr)):
            if(rStr[j] in [2,3,4,5,7]):
                rStr[j]='a'
            elif(rStr[j]==6):
                rStr[j]=9
            elif(rStr[j]==9):
                rStr[j]=6
        tmp = ''.join([str(x) for x in rStr])
        try:
            a = int(tmp)
            if(a!=i):
                # print(a)
                cnt+=1
        except:
            pass
    print(cnt)

if __name__=='__main__':
    main()
