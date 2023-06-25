# list,tuple = Duplicate data allowed
# set = No duplicate data allowed,unordered,unindexed

food = {"burger","pizza","tea"}
drinks = {"tea","coffee","milkshake"}

food.union(drinks)
food.intersection(drinks)
food.update(drinks)

# dictionary

Capitals ={'Nepal':'Kathmandu','India':'New delhi','China':'Beijing'}

Capitals.update({'Japan':'Tokyo'})
Capitals.pop('India')
Capitals.clear()

print(Capitals.keys())
print(Capitals.values())
print(Capitals.get('Nepal'))    

for key,value in Capitals.items():
    print(key,value)