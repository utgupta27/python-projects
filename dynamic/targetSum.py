def memoisation(func):
    cache = {}
    def inner(target,nums):
        key = target
        if key not in cache:
            cache[key]= func(target,nums)
        return cache[key]
    return inner



@memoisation
def targetSumArray(target,nums):
    if target == 0 : return []
    if target < 0 : return None
    smallest = None
    for i in nums:
        remainder = target - i
        result = targetSumArray(remainder,nums)
        if result != None:
            array =result + [i]
            if smallest == None or len(array)<len(smallest):
                smallest= array
    return smallest

print(targetSumArray(200,[3,4,7,5]))