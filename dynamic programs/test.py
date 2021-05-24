# to calculate all the possible combinations of given numbers that sum up to give the targeted number

def memoisation(func):
    cache = {}
    def inner(targetValue,givenValues):
        key = targetValue
        if key not in cache:
            cache[key] = func(targetValue,givenValues)
        return  cache[key]
    return inner

@memoisation
def calculate(targetValue,givenValues):
    if targetValue == 0 : return 1
    if targetValue < 1 : return 0
    count = 0 
    for i in givenValues:
        remainder = targetValue - i
        temp = calculate(remainder,givenValues)
        count += temp
    return count

# print(calculate(8,[2,3,5]))

# def displayCombination(targetValue,givenValues):
#     if targetValue == 1 : return []
#     if targetValue < 1 : return None
#     combination = []
#     for value in givenValues:
#         remainder = targetValue - value
#         temp = displayCombination(remainder,givenValues)
#         if temp != None :
#             combination.append(value)
#         return combination
#     return None

# print(displayCombination(8,[2,3,5]))