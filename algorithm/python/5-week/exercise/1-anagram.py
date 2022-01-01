#201904014 Dong Joon Oh
def is_anagram(str1, str2):
    # 두 문자열을 정렬한 후 같은 문자열인지 확인
    if ''.join(sorted(str1)) == ''.join(sorted(str2)): 
        return True
    else:
        return False

def main():

    s1,s2 = input().replace("\ufeff", "").split()

    s1 = s1.strip().lower().replace(" ", "")
    s2 = s2.strip().lower().replace(" ", "")
    if(is_anagram(s1, s2)):
        print(True)
    else:
        print(False)

if __name__=='__main__':
    main()