def perm(input_list):
    length = len(input_list)
    if length==1:
        return [input_list]
    else:
        result = []
        for i in input_list:
            temp = input_list.copy()
            temp.remove(i)

            for j in perm(temp):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
    return result

def myPerm(input_list):
    if(len(input_list)==1): return [input_list]
    result_list = []
    for i in input_list:
        headList = [i]
        tmp1 = input_list.copy()
        tmp1.remove(i)

        tmp2 = myPerm(tmp1)
        for tailList in tmp2:
            result_list.append(headList + tailList)
    return result_list

def main():
    n = int(input().replace('\ufeff','').strip())
    nlist = [x for x in range(1,n+1)]
    print(*perm(nlist))
    print(*myPerm(nlist))

if __name__=='__main__':
    main()