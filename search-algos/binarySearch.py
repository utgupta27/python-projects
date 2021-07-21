def binarySearch(arr, left, right, key):
    if right >= left:
        mid  = left + (right - left) // 2
        
        if arr[mid] == key:
            return mid
        
        if arr[mid] > key :
            return binarySearch(arr, left, mid-1, key)
        else:
            return binarySearch(arr, mid+1, right, key)

    else:
        return -1

x = [1,2,3,4,5,6,7,8,9]
print(binarySearch(x,0,len(x)-1, 8))