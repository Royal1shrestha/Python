from tkinter import *
from tkinter import filedialog

def openfile():
    ofile = filedialog.askopenfilename(#initialdr="C://bdcij//",
                                       title="Open file??",
                                       filetypes= (("text files","*.txt"),("all files","*.*")))

    file = open(ofile,'r')
    print(file.read())
    file.close()
    
def savefile():
    sfile = filedialog.asksaveasfile(defaultextension=".txt",
                                     filetypes=[("Text file",".txt"),
                                                ("HTML file",".html"),
                                                ("All files","*.")])
    
    if sfile is None:
        return
    filetext = str(text.get(1.0,END))
    sfile.write(filetext)
    sfile.close()
    

window = Tk()

button = Button(text="Open",command=openfile)
button.pack()
button = Button(text="Save",command=savefile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()