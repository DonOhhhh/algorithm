def is_palindrome(s):
    return s == s[::-1]

def main():
    input_count = int(input().replace('\ufeff',''))
    word_list = [input().replace('\ufeff','').strip() for i in range(input_count)]
    [print(True) if is_palindrome(s) else print(False) for s in word_list]

if __name__=='__main__':
    main()