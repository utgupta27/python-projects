def check(num):
    if num%2!=0:
        print('Weird')
    else:
        if num>=2 or num<=5 :
            print('Not Weird')
        elif num>=6 or num<=20:
            print('Weird')
        elif num>20:
            print('Not Weird')
        else:
            pass
if __name__ == '__main__':
    n = int(input().strip())
    check(n)