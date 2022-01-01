def is_anagram(str1, str2):
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
        return True
    else:
        return False

def main():
    input_count = int(input().replace("\ufeff",""))

    for i in range(input_count):
        word1 = input().strip().lower().replace(" ", "")
        word2 = input().strip().lower().replace(" ", "")
        print(word1, word2)
        if(is_anagram(word1, word2)):
            print(True)
        else:
            print(False)

if __name__=='__main__':
    main()