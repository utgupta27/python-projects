from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("Button Style")
root.geometry('300x250')
style=Style()
style.configure('TButton',font=('calibri',10,'bold','underline'),foreground='red')
bt1=Button(root,style='TButton',command=root.destroy,text='Quit')
bt2=Button(root,text='start',command = None)
bt1.grid(row=0,column=3,padx=150)
bt2.grid(row=1,column=3,pady=10,padx=150)
mainloop()