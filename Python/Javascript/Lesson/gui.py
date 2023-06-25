from tkinter import *

window = Tk() #an instance of window
window.geometry("720x480")
window.title("First GUI program")

icon = PhotoImage(file="C:\\Users\\Admin\\Pictures\\Saved Pictures\\pic.png") #picture must be in png format
window.iconphoto(True,icon)
window.config(background="blue") # can also put color code like #5cfcff

label = Label(window,text="Hi! How r u doing?",font=('arial',20,'bold'),fg='green',bg='red',image=icon,compound="bottom")
label.pack() #appear text in center at top
label_1 = Label(window,text="Good Morning",font=('roman',10,'italic'),relief=RAISED,bd=10,padx=10,pady=10)
label_1.place(x=0,y=0)


window.mainloop() #place window screen on pc