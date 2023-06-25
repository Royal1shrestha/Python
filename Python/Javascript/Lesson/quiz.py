def start_game():
    que_no = 1
    correct_guess = 0
    guesses = []
    
    for key in question:
        print(que_no , ". " , key)
        for i in option[que_no-1]:
            print(i)
        choice = input("Enter any one (A,B,C or D) : ").upper()
        print("\n")    
        guesses.append(choice)   
        que_no +=1
        
        correct_guess += check_answer(choice, question.get(key))
    
    display_score(correct_guess,guesses)    
            
def check_answer(choice, answer):
    if(choice == answer):
        return 1
    
    else:
        return 0
    
def display_score(score,guess):
    print("Your score is ",score,"/",len(question))
    print("Answers")
    for i in question:
        print(question.get(i), end=" ")
    
    print("\n")
    print("Guesses")    
    for i in guess:
        print(i, end=" ")
    print("\n")
    play_again()

def play_again():
    answer = input("Do you wanna play again (Yes/No)").lower()
    if(answer == "yes"):
        start_game()
        
    else:
        print("Thank you for playing the game!")

question = {'Which is a prime number?':'A',
            'When did world war II end?':'C',
            'Who is the father of computer science?':'A',
            'What is the most populated city of the world?':'D'}

option =[['A. 3' , 'B. 4' , 'C. 12' , 'D. 15'],
         ['A. 1945' , 'B. 1943' , 'C. 1947' , 'D. 1951'],
         ['A. Charles Babbage' , 'B. Sir Issac Newton' , 'C. Albert Einstein' , 'D. Bill Gates'],
         ['A. Delhi' , 'B. Shanghai' , 'C. Seoul' , 'D. Tokyo']]

start_game()