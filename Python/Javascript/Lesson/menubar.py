from tkinter import *
from tkinter import filedialog

window = Tk()

def openFile():
    ofile = filedialog.askopenfilename(#initialdr="C://bdcij//",
                                       title="Open file??",
                                       filetypes= (("text files","*.txt"),("all files","*.*")))

    file = open(ofile,'r')
    print(file.read())
    file.close()

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Open',command=openFile)
# filemenu.add_command(label='Save',command=saveFile)
filemenu.add_command(label='Close',command=quit)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=quit)

editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')

window.mainloop()