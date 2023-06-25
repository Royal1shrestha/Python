# for loop = limited
# while loop = unlimited

import time

for i in range(10):
    print(i)
    
for i in range(1,10,2):
    print(i)    
    
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("The journey begins now.")    

# nested loop

rows = int(input("Enter the no of rows?: "))
columns = int(input("Enter the no of columns?: "))

for i in range(rows):
    for j in range(columns):
        print("$",end="")
    print()