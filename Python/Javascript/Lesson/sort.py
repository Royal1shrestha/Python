list =["apple","banana","grape","cheery","blueberry"]
fruit =["papaya","watermelom","grape","pomegranate","blueberry"]

list.sort()
fruit.sort(reverse=True)

for i in list:
    print(i)

print("") 
   
for j in fruit:
    print(j)
    
tuple = [("Ram",19,1),
         ("Hari",21,4),
         ("Shyam",20,2)]

# if no key is given it takes first keyword in tuple by default.
age = lambda ages:ages[2]
tuple.sort(key=age)
for i in tuple:
    print(i)