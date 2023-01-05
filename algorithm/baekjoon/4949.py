import re
pat1 = re.compile("[\(\)\[\]]")
while (s := input()) != ".":
    s = ''.join(pat1.findall(s))
    while re.search('(\(\))|(\[\])',s):
        s = re.sub('(\(\))|(\[\])','',s)
    print('no' if s else 'yes')
