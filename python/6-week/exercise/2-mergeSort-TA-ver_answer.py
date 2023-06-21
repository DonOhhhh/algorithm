#201904014 Dong Joon Oh
class byunghapSort():
    def __init__(self) -> None:
        self.cnt = 0
        self.m = 0
        self.original = []

    def mergeSort(self,li,w):
        if(len(li)<=1): return li
        mid=len(li)//2
        left,right = li[:mid],li[mid:]
        left,right = self.mergeSort(left,w),self.mergeSort(right,w)
        return self.merge(left,right, w)

    def merge(self,left, right, w):
        result = []
        point = self.original.index(left[0])
        while(left and right):
            if(w=='A'):
                if(left[0] <= right[0]):
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            else:
                if(left[0] >= right[0]):
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            
        result += left+right
        self.cnt+=1
        self.original = (self.original[:point] + result + self.original[point+len(result):])
        # print(self.cnt,end=' : ')
        if(self.cnt == self.m): print(*self.original)
        return result

    def main(self):
        n,m,w = input().replace('\ufeff','').split()
        input_list = list(input().replace('\ufeff','').split())
        self.original = input_list
        self.m = int(m)
        self.mergeSort(input_list,w)
        # print(*self.mergeSort(input_list,w))

if __name__=='__main__':
    a = byunghapSort()
    a.main()
