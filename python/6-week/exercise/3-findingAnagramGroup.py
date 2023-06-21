#201904014 Dong Joon Oh
def isAnagram(s1,s2):
    return True if(''.join(sorted(s1)) == ''.join(sorted(s2))) else False

def findingAnagram(s_list):
    result = []
    
    for i in s_list:
        anagramExist = False
        tmp = []
        tmp.append(i)
        for j in s_list:
            if(i==j): continue
            if(isAnagram(i,j)):
                tmp.append(j)
                anagramExist = True
        tmp = sorted(tmp)
        if(not(tmp in result)):
            result.append(tmp)
            
    return sorted(result,key=lambda x: x[0])

def main():
    s_list = input().replace('\ufeff','').split()
    s_list = [x.lower() for x in s_list]
    result = findingAnagram(s_list)
    for i in result: print(*i)

if __name__=='__main__':
    main()