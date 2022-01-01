def main():
    while True:
        try:
            data = int(input().replace('\ufeff','').strip())
            if data%2==0:
                print('Hello, Coding Test!')
            else:
                print('Hello, Algorithm!')
        # ctrl+z가 입력되면 EOFError가 발생함.
        except EOFError:
            break

if __name__=='__main__':
    main()