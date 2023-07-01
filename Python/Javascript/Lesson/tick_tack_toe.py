from tkinter import *
import random

def new_game():
    pass

def next_turn(row,column):
    pass

def check_winner():
    pass

def empty_space():
    spaces = 9 
    
    for row in range(3):
        for column in range(3):
            if board[row][column]["text"] != "":
                

window = Tk()
window.title("Tic-Tac-Toe")
moves = ["X","O"]
player = random.choice(moves)

board = [[0,0,0],[0,0,0],[0,0,0]]

label = Label(text = player+" turn",font=('consolas',40))
label.pack(side=TOP)

restart_button = Button(text="Restart",font=('consolas',15),command=new_game)
restart_button.pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame,
                                    font=('consolas',30),
                                    width=5,
                                    height=2,
                                    command=lambda row=row,column=column:next_turn(row,column))
        board[row][column].grid(row=row,column=column)

window.mainloop()