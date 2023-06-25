import random

choices =["rock","paper","scissors"]

while True:

    pick = random.choice(choices)
    human = None

    while human not in choices:
        human = input("rock,paper or scissors? ").lower()

    if(pick == human):
        print("Computer : "+pick)
        print("Player : ",human)
        print("Tie !")
        
    elif(human == "rock"):
        if(pick == "scissors"):
            print("Computer : "+pick)
            print("Player : ",human)
            print("Player wins !")
            
        else:
            print("Computer : "+pick)
            print("Player : ",human)
            print("Computer wins !")

    elif(human == "paper"):
        if(pick == "rock"):
            print("Computer : "+pick)
            print("Player : ",human)
            print("Player wins !")
            
        else:
            print("Computer : "+pick)
            print("Player : ",human)
            print("Computer wins !")

    else:
        if(pick == "paper"):
            print("Computer : "+pick)
            print("Player : ",human)
            print("Player wins !")
            
        else:
            print("Computer : "+pick)
            print("Player : ",human)
            print("Computer wins !")
    
    play_again = input("Do you wanna play again ? (Yes/No) : ").lower()      
    if(play_again != "yes"):
        break
    
print("Thank you for playing.")