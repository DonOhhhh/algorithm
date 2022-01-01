#201904014 Dong Joon Oh
def bubbleSort(n,m,w,input_list):
    for i in range(n):
        if(i==m): break
        for j in range(n-1):
            haveToChange = False
            if(w=='A'):
                if(input_list[j] > input_list[j+1]): haveToChange=True
            elif(w=='D'):
                if(input_list[j] < input_list[j+1]): haveToChange=True
            if(haveToChange):
                input_list[j],input_list[j+1] = input_list[j+1], input_list[j]
        # print(input_list)
    return input_list

def main():
    n,m,w = input().replace('\ufeff','').split()
    input_list = list(input().replace('\ufeff','').split())
    # print(*bubbleSort(int(n),int(m),w,input_list))
    print(*[n,m,w])
    print(*input_list)

if __name__=='__main__':
    main()