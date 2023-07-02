from tkinter import *
import random

def new_game():
    global player
    
    player = random.choice(moves)
    label.config(text=(player+" turn"))
    
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",bg="#F0F0F0")
            
    spaces = 9

def next_turn(row,column):
    global player
    
    if board[row][column]["text"] == "" and check_winner() is False:
        if player == moves[0]:
            board[row][column]["text"] = player
            
            if check_winner() is False:
                player = moves[1]
                label.config(text=(moves[1]+' turn'))
                
            elif check_winner() is True:
                label.config(text=(moves[0]+' wins'))
                
            elif check_winner() == 'Tie':
                label.config(text='Tie!')
                
        else:
            board[row][column]["text"] = player
            
            if check_winner() is False:
                player = moves[0]
                label.config(text=(moves[0]+' turn'))
                
            elif check_winner() is True:
                label.config(text=(moves[1]+' wins'))
                
            elif check_winner() == 'Tie':
                label.config(text='Tie!')

def check_winner():
    for column in range(3):
        if board[0][column]['text'] ==  board[1][column]['text'] == board[2][column]['text'] != "":
            board[0][column].config(bg="green")
            board[1][column].config(bg="green")
            board[2][column].config(bg="green")
            return True
        
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":
            board[row][0].config(bg="green")
            board[row][1].config(bg="green")
            board[row][2].config(bg="green")
            return True
        
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        board[0][0].config(bg="green")
        board[1][1].config(bg="green")
        board[2][2].config(bg="green")
        return True
    
    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        board[0][2].config(bg="green")
        board[1][1].config(bg="green")
        board[2][0].config(bg="green")
        return True
    
    elif empty_space() is False:
        for row in range(3):
            for column in range(3):
                board[row][column].config(bg="red")
        return "Tie"
    
    else:
        return False
            
def empty_space():
    spaces = 9 
    
    for row in range(3):
        for column in range(3):
            if board[row][column]["text"] != "":
                spaces -= 1
                
    if spaces == 0:
        return False
    else:
        return True

window = Tk()
window.title("Tic-Tac-Toe")
moves = ["X","O"]
player = random.choice(moves)

board = [["","",""],["","",""],["","",""]]

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