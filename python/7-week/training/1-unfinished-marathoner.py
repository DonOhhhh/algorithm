import collections

def compareCollections(p,c):
    i = collections.Counter(p) - collections.Counter(c)
    return list(i.keys())

def main():
    a = input().replace('\ufeff','').split()
    b = input().replace('\ufeff','').split()
    print(*compareCollections(a,b))

if __name__=='__main__':
    main()

# Hash