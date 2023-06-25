name = ["Royal","Soya","Unika","Pralex","Manjil"]

name[0] = "Ram"
    
name.append("Shyam")
name.remove("Unika")
name.insert(2,"Hari")
name.sort()
name.reverse()

for i in name:
    print(i)
 
# 2D lists

breakfast = ["tea","coffee","bread"]
lunch = ["momo","sandwich","pizza"]
dinner = ["rice","wheat"]

food=[breakfast,lunch,dinner]

print(food[1][1])