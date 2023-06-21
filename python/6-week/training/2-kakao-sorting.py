import re

def file_name_sort(fname_list):
    p = re.compile('(\D+)(\d+)')
    fname_list.sort(key=lambda x: (p.match(x).group(1).lower(), int(p.match(x).group(2))))
    return (fname_list)

if __name__ == '__main__':
    c = int(input().replace('\ufeff','').strip())
    for t in range(c):
        fname_list = []
        fname_list = list(x.strip() for x in input().replace('\ufeff','').split(','))
        result = file_name_sort(fname_list)
        print(*result)