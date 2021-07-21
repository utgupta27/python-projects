def linearSearch(arr,item):
    res = False
    for i in range(len(arr)):
        if arr[i] == item:
            res = [True,i]
    return res        



if __name__ == '__main__':
    lst = [1,23,5,6,57,56,2,98,89,76,12,67]
    key= 76
    print(linearSearch(lst,key))