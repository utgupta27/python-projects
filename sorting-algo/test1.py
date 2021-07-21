# Implementation of Quick Sort Algorithm

def quickSort(start, end, arr):
    if start < end:
        p = quickPartition(start, end, arr)
        quickSort(start, p-1, arr)
        quickSort(p+1, end, arr)


def quickPartition(start, end, arr):
    pivotIndex = start
    pivot = arr[start]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start],arr[end] = arr[end], arr[start]
    arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]
    return end


if __name__ == "__main__":
    lst0 = [9,7,5,3,1,8,6,4,3,0,34,65,343,79,90,85,21,79,57,49,61,62,63,88,77,66,55,44,33,22,11,100,99]
    quickSort(0,len(lst0)-1,lst0)
    print(lst0)