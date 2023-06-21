def is_anagram(str1, str2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(str1)):
        pos = ord(str1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(str2)):
        pos = ord(str2[i]) - ord('a')
        c2[pos] += 1
    
    stillOk = True
    j = 0
    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j+=1
        else:
            stillOk = False
    return stillOk

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