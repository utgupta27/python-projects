def triangle(n):
    k=n*2-2
    for i in range(n):  
        for j in range(k):
            print(" ",end='')
        for l in range(i+1):
            print(" *",end='')
        k=k-2
        for i in range(i):
            print(" *",end='')
        print('')

triangle(int(input("Enter a number: ")))
