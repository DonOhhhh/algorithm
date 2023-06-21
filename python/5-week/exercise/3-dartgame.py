#201904014 Dong Joon Oh
import re

def getScore(input_string):
    p = re.compile("(\d+)([a-zA-z])(\*|\#)?")
    sliced_string = p.findall(input_string)

    result = []
    bonusNum = 0

    # 먼저 *옵션을 빼고 계산한다.
    for i, score in enumerate(sliced_string):
        point = score[0]
        bonus = score[1]
        option = score[2]
        if bonus == 'S': bonusNum = 1
        elif bonus == 'D': bonusNum = 2
        elif bonus == 'T': bonusNum = 3

        if option == '#':
            result.append(int(point)**bonusNum*-1)
        else:
            result.append(int(point)**bonusNum)
    
    # 다시 돌면서 뒤에서부터 * 옵션이 있는지 확인하여 계산한다.
    for i,score in enumerate(sliced_string):
        point = score[0]
        bonus = score[1]
        option = score[2]
        if bonus == 'S': bonusNum = 1
        elif bonus == 'D': bonusNum = 2
        elif bonus == 'T': bonusNum = 3

        if option == '*':
            result[i] *= 2
            if(i!=len(sliced_string)-1):
                result[i+1] *= 2
    
    return sum(result)

def main():
    s = input().replace('\ufeff','')
    print(getScore(s))

if __name__=='__main__':
    main()