from tkinter import *
root=Tk()
root.title("Practice")
root.geometry("600x400")
lb=Label(root,text="color Boxes").pack()
f=Frame(root,background="black")
bt1=Button(f,fg="red",activebackground="red",text="red").pack(side=LEFT)
bt2=Button(f,fg="yellow",activebackground="yellow",text="yellow").pack(side=RIGHT)
bt3=Button(f,fg="blue",activebackground="blue",text="blue").pack(side=BOTTOM)
bt4=Button(f,fg="green",activebackground="green",text="green").pack(side=TOP)
f.place(width=200,height=200,x=100,y=100)
mainloop()

