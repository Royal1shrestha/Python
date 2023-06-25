from tkinter import *

window = Tk()

def submit():
    print("The temperature is ",scale.get(),"C")
    
scale = Scale(window,
              from_=100,
              to=0,
              orient="vertical",
              length=300,
              font=('Consolas',10),
              tickinterval=10
              )
scale.pack()

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)


window.mainloop()