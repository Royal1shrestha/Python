# break = used to terminate thr loop entirely
# continue = used to skip to next part of the iteration of loop
# pass = skips the part

# while True:
#     name = input("Enter your name?: ")
#     if name !="":
#         break
    
phone_no = "980-375-7204"

for i in phone_no:
    if i == "-":
        continue
    print(i,end="")
    
for i in range(10):
    if i == 7:
        pass
    else:
        print(i)