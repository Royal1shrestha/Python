from tkinter import *

window = Tk()
photo = PhotoImage(file="C:\\Users\\Admin\\Pictures\\Saved Pictures\\pic.png")
count = 0
def click():
    global count
    count +=1
    print("You have pressed the button ",count," times.")
    
button = Button(window,text="Click Here",command=click,background='black',bg='yellow',fg='green',state=ACTIVE,image=photo)
button.pack()
window.mainloop()