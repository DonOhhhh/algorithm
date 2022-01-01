import bisect

def getMinPower(base,power):
    d = []
    for b in base:
        x = bisect.bisect(power,b)
        if(x==0):
            d.append(abs(power[x]-b))
        elif(x==len(power)):
            d.append(abs(power[x-1]-b))
        else:
            d.append(min(abs(power[x]-b),abs(power[x-1]-b)))
    return max(d)

def main():
    base = sorted(list(map(int,input().split())))
    power = sorted(list(map(int,input().split())))
    print(getMinPower(base,power))

if __name__=='__main__':
    main()