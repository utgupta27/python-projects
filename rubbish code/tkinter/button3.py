from tkinter import *
from tkinter.ttk import *

root = Tk() 
root.geometry('300x250') 

style = Style() 
style.configure('TButton', font =
			('calibri', 20, 'bold'), 
					borderwidth = '50') 

# Changes will be reflected 
# by the movement of mouse. 
style.map('TButton', foreground = [('active', 'green')], 
					background = [('active', 'black')]) 

# button 1 
btn1 = Button(root, text = 'Quit !', command = root.destroy) 
btn1.grid(row = 0, column = 3, padx = 80) 

# button 2 
btn2 = Button(root, text = 'Click me !', command = None) 
btn2.grid(row = 1, column = 3, pady = 0, padx = 80) 

root.mainloop() 
