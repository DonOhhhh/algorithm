def getMaxRoute(n,m,matrix):
    start = max(matrix[0])
    loc = matrix[0].index(start)
    energySum = start

    # print(loc)
    for i in range(1,m):
        try:
            maxEnergy = max(matrix[i][loc-1:loc+2])
        except:
            if(loc-1 < 0):
                maxEnergy = max(matrix[i][loc:loc+2])
            elif(loc+1 == len(matrix[i])):
                maxEnergy = max(matrix[i][loc-1:])
        loc = matrix[i].index(maxEnergy)
        # print(loc)
        energySum += maxEnergy
    return energySum

def main():
    n,m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(m)]
    print(getMaxRoute(n,m,matrix))

if __name__=='__main__':
    main()