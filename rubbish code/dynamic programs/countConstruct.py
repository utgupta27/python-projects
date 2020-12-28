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
    print("start")
    if targetString == '' :
        print("returned 1")
        return 1
    count = 0
    print("count =0")
    for word in wordBank:
        print("for loop")
        if targetString.find(word) == 0 :
            suffix = targetString[len(word):]
            print(suffix)
            temp = countConstruct(suffix,wordBank)
            count  += temp
            print(str(temp)+"  temp")
            print(str(count)+"  count")
    print("end")
    return count

print(countConstruct("purple",["purp","p","le","ur","purpl","purple"]))

#print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))

#print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeee",["e","ee","eee","eeee","eeeee"]))
    
