import sys
from copy import deepcopy
from collections import Counter
input = sys.stdin.readline

def getAllStr(s,subseq=[],results=[]):
    if(not s): return
    for i in range(0,len(s)):
        subseq.append(s[i])
        results.append(''.join(subseq))
        getAllStr(s[i+1:],subseq,results)
        subseq.pop()
        if(''.join(subseq) not in results): results.append(''.join(subseq))
    return results

def lcs_recursion(long, short):
    longSet = list(filter(lambda x: x!='',getAllStr(long,[],[])))
    shortSet = list(filter(lambda x: x!='',getAllStr(short,[],[])))
    print(longSet)
    print(shortSet)
    result = []
    for i in range(len(shortSet)):
        if(shortSet[i] in longSet): result.append(shortSet[i])
    return result

def getAllStr_mem(s):
    return

def lcs_dp_memoization(long,short):
    return

def main():
    str1 = input().strip()
    str2 = input().strip()
    result = lcs_recursion(str1,str2) if(len(str1) >= len(str2)) else lcs_recursion(str2,str1)
    print(result)

if __name__=='__main__':
    main()