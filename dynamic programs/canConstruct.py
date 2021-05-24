def memoisation(func):
    cache = {}
    def inner(targetWord,wordBank):
        key= targetWord
        if key not in cache:
            cache[key]=func(targetWord,wordBank)
        return cache[key]
    return inner

@memoisation
def canConstructSuffix(targetWord,wordBank):
    if targetWord == '' : return True
    for word in wordBank:
        if targetWord.find(word) == 0 :
            suffix = targetWord[len(word):]
            if canConstructSuffix(suffix,wordBank):
                return True
    return False

def canConstructPrefix(targetWord,wordBank):
    if targetWord == '' : return True
    for word in wordBank:
        if targetWord.find(word) != -1 :
            prefix = targetWord[:-len(word)]
            if canConstructPrefix(prefix,wordBank):
                return True
    return False

# print(canConstructPrefix('helloworld',['hel','rld','lo','wo']))
print(canConstructSuffix('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeel',['e','ee','eee','eeee']))