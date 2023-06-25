from tkinter import *

window = Tk()

def submit():
    name = entry.get()
    print("Hello",name)
    
def delete():
    entry.delete(0,"end")
    
def backspace():
    entry.delete(len(entry.get())-1,"end")
    
def display():
    if(x.get()) == 1:
        print("You agree.")
    else:
        print("You don't agree.")
    
x=IntVar()

entry = Entry(window,font=('Arial',50))
# entry = Entry(window,font=('Arial',50),show="*") used for not showing password
entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)

check_button = Checkbutton(window,
                      text="I agree to the terms and conditions",
                      variable=x,
                      onvalue=1,
                      offvalue=0,
                      command=display)
check_button.pack(side=LEFT)

window.mainloop()