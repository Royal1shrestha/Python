import random

# print any number between 1 and 5
print(random.randint(1,5))

# print any number between 0 and 1
print(random.random())

mylist = ['hand','leg','head']
print(random.choice(mylist))

cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
random.shuffle(cards)
print(cards)