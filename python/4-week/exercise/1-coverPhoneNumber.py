if __name__ == '__main__':
    phone_number = input().replace('\ufeff','').replace('-','')
    print('*'*(len(phone_number)-4) + phone_number[len(phone_number)-4:])
