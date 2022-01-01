n,k,i = map(int,input().split())
num_list = [int(i) for i in input().split()]
num_list.sort()
print(num_list[k-1]+num_list[n-i])
