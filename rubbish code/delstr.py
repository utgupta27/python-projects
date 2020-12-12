def findstr(str,pattern):
    tmp=str.find(pattern)
    str2=str[0:tmp] + str[(tmp+len(pattern)):]
    print(str2)
str=input("Enter a string: ")
pattern=input("Input a Pattern: ")
findstr(str,pattern)