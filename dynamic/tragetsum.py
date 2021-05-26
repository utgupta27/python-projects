def memoisation(func):
    memory = {}
    def inner(target,nums):
        key = target
        if key not in memory:
            memory[key] = func(target,nums)
        return memory[key]
    return inner

@memoisation
def canSum(target,nums):
    if target == 0: return True
    if target<0: return False
    for i in nums:
        rem = target - i
        if canSum(rem,nums) == True : return True
    return False

print(canSum(20,[1,7,3]))