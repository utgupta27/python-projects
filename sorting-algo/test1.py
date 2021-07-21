def linearSearch(arr,key):
    res = -1
    for i in range(len(arr)):
        if key == arr[i]:
            res = i
            return res
    return res



if __name__ == "__main__":
    lst = [0,1,2,3,4,5,6,6,6,6,7,8,9]
    print(linearSearch(lst,6))