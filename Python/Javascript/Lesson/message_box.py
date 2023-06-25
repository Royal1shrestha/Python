def click():
    # messagebox.showinfo(title='Info box',message='This is info.')
    # messagebox.showerror(title='Info box',message='This is info.')
    # messagebox.showwarning(title='Info box',message='This is info.')
    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to or not?'):
    #     print("You wanted it.")
    # else:
    #     print("You cancelled it.")
        
    if messagebox.askquestion(title='ask question',message='Do you want like momo?'):
        print("I like it too.")
    else:
        print("Why don't you like it??")

from tkinter import *
from tkinter import messagebox

window = Tk()

click_button = Button(window,text='click me',command=click)
click_button.pack()

window.mainloop()