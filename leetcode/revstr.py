class rev:
    def __init__(self,str):
        self.str=str
        self.idx=len(str)
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx==0:
            raise StopIteration
        else:
            self.idx-=1
            return self.str[self.idx]
def main():
    str=input("Enter a string: ")
    obj= rev(str)
    for i in obj:
        print(i)

if __name__ == "__main__":
    main()