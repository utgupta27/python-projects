def main(array):
    quickSort(0,len(array)-1,array)

def quickSort(start, end, array):
    if start < end :
        p = partition(start, end, array)
        quickSort(start, p-1, array)
        quickSort(p+1, end, array)


def partition(start, end, array):
    # taking start element as a pivot
    pivotIndex = start
    pivot = array[pivotIndex]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if(start < end):
            array[start], array[end] = array[end], array[start]
    
    array[end], array[pivotIndex] =array[pivotIndex],array[end]
    return end

if __name__ == "__main__":
    lst0 = [9,7,5,3,1,8,6,4,3,0,34,65,343,79,90,85,21,79,57,49,61,62,63,88,77,66,55,44,33,22,11,100,99]
    main(lst0)
    print(lst0)
