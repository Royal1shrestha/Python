def submit():
    print(listbox.get(listbox.curselection()))
 
# for multiple mode   
# def submit():
#     hero = []
#     for i in listbox.curselection():
#         hero.insert(i,listbox.get(i))
        
#     for i in hero:
#         print(i)

# def delete():
#     for i in reversed(listbox.curselection()):
#         listbox.delete(i)
    
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
    
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
    
from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="grey",
                  font=('Constansia',25),
                  #selectmode=MULTIPLE, #to select multiple data
                  width=10)
listbox.pack()

listbox.insert(1,"Tank")
listbox.insert(2,"Mage")
listbox.insert(3,"Assasin")
listbox.insert(4,"Marksman")
listbox.insert(5,"Support")
listbox.insert(6,"Fighter")

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

button_1 = Button(window,text='submit',command=submit)
button_1.pack()
button_2 = Button(window,text='add',command=add)
button_2.pack()
button_3 = Button(window,text='delete',command=delete)
button_3.pack()

window.mainloop()