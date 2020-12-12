import os
print("\nThe path is :\n")
a= os.getcwd()
os.remove(a+'\data.txt')
print(a+'\data.txt')
