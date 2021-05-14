def canSum(target,lst,cache = {}):
    if target in cache : return cache[target]
    if target < 0 : return False
    if target == 0 : return True
    for item in lst:
       if canSum(target - item,lst) == True:
            cache[target] = True
            return cache[target]
    cache[target] = False
    return False

if __name__ == '__main__':
    print(canSum(300,[2,15]))
