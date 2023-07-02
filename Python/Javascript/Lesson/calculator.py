from tkinter import *

def button_push(num):
    global eq_text
    eq_text = eq_text + str(num)
    eq_label.set(eq_text)
 
def button_equal():
    global eq_text
    try:
        total = str(eval(eq_text))
        eq_label.set(total)
        eq_text = total
        
    except Exception:
        eq_label.set("Error!")
        eq_text = ""

def button_backspace():
    global eq_text
    eq_text = eq_text[:-1]
    eq_label.set(eq_text)

def button_clear():
    global eq_text
    eq_text = ""
    eq_label.set(eq_text)

window = Tk()
window.title("Calculator")
window.geometry("300x300")

eq_text = ""
eq_label = StringVar()

label = Label(window,textvariable=eq_label,bg="white",width=12,height=2,font=('consolas',30))
label.pack(fill=BOTH)

frame = Frame(window)
frame.pack()


button_1 = Button(frame,command=lambda:button_push(0),text=0,width=5,height=2,font=20)
button_1.grid(row=3,column=0)
button_2 = Button(frame,command=lambda:button_push('.'),text=".",width=5,height=2,font=20)
button_2.grid(row=3,column=1)
# button_text = "x10\u207F" for supercript N characters
# button_text = "x10\u02E3" #for superscript x characters
button_3 = Button(frame,command=lambda:button_push('('),text="(",width=5,height=2,font=20)
button_3.grid(row=3,column=2)
button_4 = Button(frame,command=lambda:button_push(')'),text=")",width=5,height=2,font=20)
button_4.grid(row=3,column=3)
button_5 = Button(frame,command=lambda:button_equal(),text="=",width=5,height=2,font=20)
button_5.grid(row=3,column=4)
button_6 = Button(frame,command=lambda:button_push(1),text=1,width=5,height=2,font=20)
button_6.grid(row=2,column=0)
button_7 = Button(frame,command=lambda:button_push(2),text=2,width=5,height=2,font=20)
button_7.grid(row=2,column=1)
button_8 = Button(frame,command=lambda:button_push(3),text=3,width=5,height=2,font=20)
button_8.grid(row=2,column=2)
button_9 = Button(frame,command=lambda:button_push('+'),text="+",width=5,height=2,font=20)
button_9.grid(row=2,column=3)
button_10 = Button(frame,command=lambda:button_push('-'),text="-",width=5,height=2,font=20)
button_10.grid(row=2,column=4)
button_11 = Button(frame,command=lambda:button_push(4),text=4,width=5,height=2,font=20)
button_11.grid(row=1,column=0)
button_12 = Button(frame,command=lambda:button_push(5),text=5,width=5,height=2,font=20)
button_12.grid(row=1,column=1)
button_13 = Button(frame,command=lambda:button_push(6),text=6,width=5,height=2,font=20)
button_13.grid(row=1,column=2)
button_14 = Button(frame,command=lambda:button_push('*'),text="x",width=5,height=2,font=20)
button_14.grid(row=1,column=3)
divide_text = "\u00F7"
button_15 = Button(frame,command=lambda:button_push('/'),text=divide_text,width=5,height=2,font=20)
button_15.grid(row=1,column=4)
button_16 = Button(frame,command=lambda:button_push(7),text=7,width=5,height=2,font=20)
button_16.grid(row=0,column=0)
button_17 = Button(frame,command=lambda:button_push(8),text=8,width=5,height=2,font=20)
button_17.grid(row=0,column=1)
button_18 = Button(frame,command=lambda:button_push(9),text=9,width=5,height=2,font=20)
button_18.grid(row=0,column=2)
button_19 = Button(frame,command=lambda:button_backspace(),text="DEL",width=5,height=2,font=20)
button_19.grid(row=0,column=3)
button_20 = Button(frame,command=lambda:button_clear(),text="AC",width=5,height=2,font=20)
button_20.grid(row=0,column=4)

window.mainloop()