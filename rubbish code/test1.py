from tkinter import *
root= Tk()
root.title("Scrollbar")
root.geometry("300x300")
sb=Scrollbar(root)
sb.pack(side=RIGHT)
lb=Listbox(root,yscrollcommand=sb.set)
lb.pack(side=RIGHT)
for i in range(100):
    lb.insert(END,"this is line",str(i))
sb.config(command=lb.yview)
mainloop()