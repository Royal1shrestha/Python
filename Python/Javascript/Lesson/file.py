import os

path = "F:\\royal\\text.txt"

if os.path.exists(path):
    print("The path exists.")
    
    if os.path.isfile(path):
        print("It is a file.")
        
    elif os.path.isdir(path):
        print("It is a directive.")
        # directive refers to as folder.    
        
    else:
        print("It is neither file nor directive.")
    
else:   
    print("The print doesn't exists.")

try:    
    with open('F:\\royal\\text.txt') as file:
        print(file.read())
    
except FileNotFoundError:
    print("The file has not been found.")

text = "The file has been overwritten"       
with open('F:\\royal\\text.txt','w') as file:
    file.write(text)
    # print(file.write(text)) tells the no of characters.   
