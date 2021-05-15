def memoisation(func):
    cache= {}
    def inner(targetString,wordBank):
        key = targetString
        if key not in cache:
            cache[key] = func(targetString,wordBank)
        return cache[key]
    return inner

@memoisation
def countConstruct(targetString,wordBank):
    if targetString == '' :
        return 1
    count = 0
    for word in wordBank:
        if targetString.find(word) == 0 :
            suffix = targetString[len(word):]
            temp = countConstruct(suffix,wordBank)
            count  += temp
    return count

print(countConstruct("purple",["purp","p","le","ur","purpl","purple"]))

print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))

#print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeee",["e","ee","eee","eeee","eeeee"]))