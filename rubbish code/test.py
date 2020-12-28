def test(n):
    if  n>0:
        print(n)
        test(n-1)
        test(n-1)

test(4)
