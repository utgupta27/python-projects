def insertionSort(arr):
    # In insertion sort we always assume that the 1st element of the array 
    #  is sorted and we compare it with the next element. Then we place the next element
    # in its right position in the previously soted array in the beginning of the whole array
    for i in range(1, len(arr)):
        # Storing the value of next element into the key variable
        key = arr[i]
        # the index first element of array is 1 less than the index of second element
        j = i-1
        # Place the next element (i.e, key) at its correct position in the sorted part that is at the
        # beginning of the remaining unsorted array
        while j >= 0 and key < arr[j]:
            # shift the elements to their right to make room for the element that to be inserted 
            arr[j+1] =  arr[j]
            # decrement the value of j to traverse the sorted part of the array i.e, beginning
            j -= 1
        # insert the key element at it's right place in the sorted part of array
        arr[j+1] = key 


if __name__ == "__main__":
    lst = [4,5,3,6,2,7,1,9,8,0]
    insertionSort(lst)
    print(lst) 

