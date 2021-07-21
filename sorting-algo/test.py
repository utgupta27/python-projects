def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]

def selectionSort(arr):
    for i in range(len(arr)):
        min = i 
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return list(merge(left,right))

def merge(left,right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    
    if len(left) == 0:
        result += right
    else:
        result += left

    return result
    

def quickSort(start, end, arr):
    if start < end:
        p = partition(start,end,arr)
        quickSort(start, p-1, arr)
        quickSort(p+1, end, arr)

def partition(start, end, arr):
    pivotIndex = start
    pivot = arr[start]
    while start<end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start<end:
            arr[start],arr[end] = arr[end],arr[start]
    arr[end],arr[pivotIndex] = arr[pivotIndex],arr[end]
    return end

def main(arr):
    # driver program for quickSort
    quickSort(0,len(arr)-1,arr)

if __name__ == "__main__":
    lst0 = [9,7,5,3,1,8,6,4,3,0,34,65,343,79,90,85,21,79,57,49,61,62,63,88,77,66,55,44,33,22,11,100,99]
    lst1 = [9,7,5,3,1,8,6,4,3,0,34,65,343,79,90,85,21,79,57,49,61,62,63,88,77,66,55,44,33,22,11,100,99]
    lst2 = [9,7,5,3,1,8,6,4,3,0,34,65,343,79,90,85,21,79,57,49,61,62,63,88,77,66,55,44,33,22,11,100,99]
    lst3 = [9,7,5,3,1,8,6,4,3,0,34,65,343,79,90,85,21,79,57,49,61,62,63,88,77,66,55,44,33,22,11,100,99]
    lst4 = [9,7,5,3,1,8,6,4,3,0,34,65,343,79,90,85,21,79,57,49,61,62,63,88,77,66,55,44,33,22,11,100,99]
    bubbleSort(lst0)
    selectionSort(lst1)
    insertionSort(lst2)
    main(lst4)
    print(lst0)
    print(lst1)
    print(lst2)
    print(mergeSort(lst3))
    print(lst4)