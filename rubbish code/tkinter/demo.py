from tkinter import *
root = Tk()
root.title('demo app')
root.geometry('400x300')
btn=Button(root,activebackground="Blue",fg="green",text="Exit",command=root.destroy)
btn.place(x=350,y=250)
var1 = IntVar()
var2=IntVar()
Checkbutton(root,text="Male",variable=var1).grid(column=1,row=0)
Checkbutton(root,text="Female",variable=var2).grid(column=1,row=3)
mainloop()