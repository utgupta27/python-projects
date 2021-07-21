def mergeSort(arr):
    # This is out base condition for reccursive calls
    if len(arr) <= 1:
        return arr
    # Calculate the mid point of the array using the integer division
    mid = len(arr) // 2
    # Split the arrrays into left half and right half form the mid point
    right = arr[mid:]
    left  = arr[:mid]
    # reccursively calls itself until the array splits into its individual elements 
    left = mergeSort(left)
    right = mergeSort(right)
    # creating a list form merge function and returning the sorted array
    return list(merge(left,right))


def merge(left, right):
    # An empty list to store the resultant sorted array
    result  =  []
    # While both the sub arrays has some element in them we merge them in sorted order
    while len(left) != 0  and len(right) != 0 :
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    # Appending the remaining elements while one of the subarray is empty
    if len(left) == 0:
        result += right
    else:
        result += left
    # Returning the merged array in sorted order
    return result


if __name__ == "__main__":
    lst = [4,5,3,6,2,7,1,9,8,0]
    print(mergeSort(lst)) 