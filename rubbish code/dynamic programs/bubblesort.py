def bubbleSort(lst,n):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
    bubbleSort(lst,n-1)

if __name__== "__main__" :
    a = [0,1,9,2,8,3,7,4,6,5]
    bubbleSort(a,len(a))