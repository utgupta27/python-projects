def printCanSum(target,lst):
    if target < 0 : return None
    if target == 0 : return []

    for item in lst:
        remainder = target-item
        result = printCanSum(remainder,lst)
        if result != None:
            return result.append(item)

    return None

if __name__ == '__main__':
    print(printCanSum(7,[2,3]))