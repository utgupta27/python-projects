from tkinter import *
root =Tk()
root.title("My application")
root.geometry("300x200")
lb1 = Label(root,text="Type here something")
lb1.grid()
txt=Entry(root,width=10)
txt.grid(column=1,row=0)
def clicked():
    lb1.configure(text= "you wrote :" + txt.get())
bt1= Button(root,text="click",fg="red",command = clicked)
bt1.grid(column=2,row=0)
root.mainloop()