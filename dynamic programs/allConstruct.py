def allConstruct(targetString,wordBank):
    if targetString == 0 : return []
    a = []
    for word in wordBank:
        if targetString.find(word) == 0 :
            suffix = targetString[len(word):]
            result = allConstruct(suffix,wordBank)
            a = result + 
    return a



print(allConstruct("purple",["purp","p","le","ur","purpl","purple"]))