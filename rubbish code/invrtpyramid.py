def ipyra(n):
    k=n*2-2
    for i in range(n):
        for j in range(k):
            print(" ",end='')
        for l in range(i+1):
            print(" *",end='')
        k-=2
        print("")
if __name__ == "__main__":
    ipyra(int(input("Enter a number: ")))
