def ifelse(n):
    if (n%2==0):
        if (n>=2 & n<=5):
            print('Not Weird')
        elif (n>=6 & n<=20):
            print('Weird')
        elif n>20:
            print('Not Weird')
    else:
        print('Weird')

if __name__ == '__main__':
    n = int(input().strip())
    while(n<0 & n>100):
        n = int(input().strip())
    ifelse(n)