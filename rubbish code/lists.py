def do(lst):
    print(lst)
if __name__ == "__main__":
    lst=[]
    n=int(input())
    for i in range(n):
        lst.append(list(input().split()))
    do(lst)