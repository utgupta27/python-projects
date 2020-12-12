from tkinter import *

from func import *

root = Tk()
root.title('uText - Text Editor')
root.geometry('600x350')

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File ', menu=filemenu)
filemenu.add_command(label='New      ')
filemenu.add_command(label='Open      ')
filemenu.add_command(label='Save      ')
filemenu.add_command(label='Save As    ')
filemenu.add_separator()
filemenu.add_command(label='Close     ', command=root.destroy)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit ', menu=editmenu)
editmenu.add_command(label='Undo     ')
editmenu.add_command(label='Redo    ')
editmenu.add_separator()
editmenu.add_command(label='Cut     ')
editmenu.add_command(label='Copy     ')
editmenu.add_command(label='Paste    ')
editmenu.add_separator()
editmenu.add_command(label='Find    ')

viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Status Bar      ')

zoommenu = Menu(viewmenu, tearoff=0)
viewmenu.add_cascade(label=' Zoom', menu=zoommenu)
zoommenu.add_command(label='Zoom In')
zoommenu.add_command(label='Zoom Out')

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='View Help   ')
helpmenu.add_command(label='Send Feedback')
helpmenu.add_separator()
helpmenu.add_command(label='About Utext')

frame = Frame(root)
frame.pack(fill=BOTH, expand=1)

text_box = Text(frame, width=50, height=50, selectbackground='light green', selectforeground='brown', font='calibri')
text_box.pack(side=LEFT, fill=BOTH, expand=1)

text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)
text_scroll.config(command=text_box.yview)

root.config(menu=menubar)
root.mainloop()
