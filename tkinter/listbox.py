from tkinter import *
root=Tk()
root.title("List Box GUI Demo")
root.geometry("600x400")
def show():
    lb.grid(column=0,row=1)
def show_editlist():
    lb1.grid(column=1,row=1)
def show_sel():
    lb2.grid(column=2,row=1)
bt=Button(root,text="File",activebackground="blue",width=15,command=show)
bt.grid()
bt1=Button(root,text="Edit",width=15,command=show_editlist)
bt1.grid(column=1,row=0)
bt2=Button(root,text="Selection",activebackground="red",width=15,command=show_sel)
bt2.grid(column=2,row=0)


lb=Listbox(root)
lb.insert(1,"Open")
lb.insert(2,"Save")
lb.insert(3,"Save As")
lb.insert(4,"Exit")

lb1=Listbox(root)
lb1.insert(1,"Undo")
lb1.insert(2,"Redo")
lb1.insert(3,"Cut")
lb1.insert(4,"Copy")
lb1.insert(5,"Paste")

lb2=Listbox(root)
lb2.insert(1,"up")
lb2.insert(2,"Down")
lb2.insert(3,"Left")
lb2.insert(4,"Right")
lb2.insert(5,"Centre")
mainloop()
