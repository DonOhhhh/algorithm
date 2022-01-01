import re

def getScore(input_string):
    p = re.compile("(\d+)([a-zA-z])(\*|\#)?")
    sliced_string = p.findall(input_string)

    result = []

    for i, score in enumerate(sliced_string):
        point = score[0]
        bonus = score[1]
        option = score[2]
        if bonus == 'S': bonus = 1
        elif bonus == 'D': bonus = 2
        elif bonus == 'T': bonus = 3
        if option == "*":
            if i == 0:
                result.append(int(point)**bonus*2)
            else:
                result[-1] *= 2
                result.append(int(point)**bonus*2)
        elif option == '#':
            result.append(int(point)**bonus*-1)
        else:
            result.append(int(point)**bonus)
    
    return sum(result)

def main():
    n = int(input().replace('\ufeff',''))
    dartResult = [getScore(input().replace('\ufeff','')) for x in range(n)]
    print(dartResult)

if __name__=='__main__':
    main()