def bubbleSort(arr):
    #traverse the array
    for i in range(len(arr)):
        # For each element i traverse the array again
        # the range(len(arr)-1) works fine but to imporve the algorithm we need to eliminate the
        # unnecessary comparisons , thus range(len(arr)-i-1) is taken.
        for j in range(len(arr)-i-1):
            # if the next element is smaller than the current element, then swap them
            if arr[j] > arr[j+1]:
                # Swapping the elements
                arr[j],arr[j+1] = arr[j+1],arr[j]



if __name__ == '__main__':
    lst = [4,5,3,6,2,7,1,9,8,0]
    bubbleSort(lst)
    print(lst)