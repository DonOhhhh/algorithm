#201904014 Dong Joon Oh
def is_palindrome(s):
    return s == s[::-1]

def myLps(s):
    result = []
    lps = ''

    for k in range(1,3):
        for i in range(len(s)-k):
            start = 0
            end = 0
            if(is_palindrome(s[i:i+k+1])):
                start = i
                end = i+k+1
                while True:
                    if(start < 0 or end > len(s)):
                        break
                    else:
                        if(is_palindrome(s[start:end])):
                            # if(not(s[start:end] in result)): result.append(s[start:end])
                            lps = s[start:end] if len(s[start:end]) > len(lps) else lps
                            start -= 1
                            end += 1
                        else:
                            break


    # # 길이가 짝수인 subpalindrome을 찾는다.
    # for i in range(len(s)-1):
    #     start = 0
    #     end = 0
    #     if(is_palindrome(s[i:i+2])):
    #         start = i
    #         end = i+2
    #         while True:
    #             if(start < 0 or end > len(s)):
    #                 break
    #             else:
    #                 if(is_palindrome(s[start:end])):
    #                     # if(not(s[start:end] in result)): result.append(s[start:end])
    #                     lps = s[start:end] if len(s[start:end]) > len(lps) else lps
    #                     start -= 1
    #                     end += 1
    #                 else:
    #                     break

    # # 길이가 홀수인 subpalindrome을 찾는다.
    # for i in range(len(s)-2):
    #     start = 0
    #     end = 0
    #     if(is_palindrome(s[i:i+3])):
    #         start = i
    #         end = i+3
    #         while True:
    #             if(start < 0 or end > len(s)):
    #                 break
    #             else:
    #                 if(is_palindrome(s[start:end])):
    #                     # if(not(s[start:end] in result)): result.append(s[start:end])
    #                     lps = s[start:end] if len(s[start:end]) > len(lps) else lps
    #                     start -= 1
    #                     end += 1
    #                 else:
    #                     break

    # BruteForce
    # for i in range(len(s)-1):
    #     for j in range(i+2,len(s)+1):
    #         if(is_palindrome(s[i:j])):
    #             result.append(s[i:j])

    return lps

def main():

    s = input().replace('\ufeff','').strip().lower()
    print(myLps(s))
    
if __name__ == '__main__':
    main()