def selectionSort(arr):
    # traverse the Array
    for i in range(len(arr)):
        # let the minimum index be
        min = i
        #traverse the remaining array i.e, i+1 to len(arr)
        for j in range(i+1,len(arr)):
            # find the minimum index and assign it to minimum
            if arr[min] > arr[j]:
                min = j
        # swap the values of current element (i.e, i) with min index
        arr[i],arr[min] =  arr[min],arr[i]

if __name__ == "__main__":
    lst = [4,5,3,6,2,7,1,9,8,0]
    selectionSort(lst)
    print(lst)
