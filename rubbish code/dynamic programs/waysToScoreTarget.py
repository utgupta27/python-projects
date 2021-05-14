def memoisation(func):
    cache = {}
    def inner(parameter):
        key = parameter
        if key not in cache:
            cache[key] = func(parameter)
        return cache[key]

    return inner

@memoisation
def calculateWays(target):
    if target < 0: return 0
    if target == 0: return 1
    return calculateWays(target - 10) + calculateWays(target - 5) + calculateWays(target - 3)



if __name__ == '__main__':
    print(calculateWays(13))
