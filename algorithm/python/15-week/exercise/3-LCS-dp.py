def lcs(s1,s2):
    # 문자열을 검사할 배열을 만든다.
    arr = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1) + 1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if(s1[i-1] == s2[j-1]):
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i][j-1], arr[i-1][j])
    return arr[-1][-1]

def main():
    s1 = input()
    s2 = input()
    print(lcs(s1,s2))   

if __name__=='__main__':
    main()