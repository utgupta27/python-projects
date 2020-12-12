from tkinter import *
root =Tk()
root.title("My application")
root.geometry("300x200")
lb1 = Label(root,text="hey just click here ->")
lb1.grid()
def clicked():
    lb1.configure(text="you just clicked ")
bt1= Button(root,text="click",fg="red",command = clicked)
bt1.grid(column=1,row=0)
root.mainloop()