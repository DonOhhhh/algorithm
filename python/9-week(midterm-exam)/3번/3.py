import sys
import re

def determineType(line):

    line = line.upper()
    macRule = re.compile('([0-9]{0,2}[A-F]{0,2})')
    
    mac1 = line.split(':')
    if(len(mac1)==6):
        for n in mac1:
            if(macRule.match(n).group()==''):
                return 0
        return 'MAC'
        
    mac2 = line.split('-')
    if(len(mac2)==6):
        for n in mac2:
            if(macRule.match(n).group()==''):
                return 0
        return 'MAC'
    
    ip = line.split('.')
    if(len(ip)==4):
        for n in ip:
            try:
                if(int(n) < 0 or int(n) > 255):
                    return 0
            except:
                return 0
        return 'IP'
    return line

def main():
    # print(determineType(input()))
    for line in sys.stdin.readlines(): 
        print(determineType(line.replace('\ufeff','').strip()))
        # print(line.replace('\ufeff','').strip())

if __name__=='__main__':
    main()