def twoSum(lst,target):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if(lst[i] + lst[j] == target):
                return [i,j]
                break

if __name__ == '__main__':
    print(twoSum([7,8,19,2,20],9))