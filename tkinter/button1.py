from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("Button demo")
root.geometry('300x250')
style=Style()
style.configure('TButton',font=('calibri',10,'bold','underline'),foreground ='red')
btn=Button(root,style='TButton',text='Quit',command=root.destroy)
btn.pack(side=TOP)
mainloop()