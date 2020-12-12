def pyr(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print("")

pyr(int(input("Enter a number: ")))
