# map() = apply functon to each of the iterative(list,tuple,...)
# map(function,iterable)

price = [("shirt",500),
         ("pant",1000),
         ("jacket",1200)]

to_npr = lambda money : (money[0],money[1]*1.6)
change = list(map(to_npr,price))

for i in change:
    print(i)
    
# filter(function,iterable)

people =[("Ram",15),
         ("Shyam",18),
         ("Hari",19),
         ("Geeta",17),
         ("Sita",18)]

name = lambda data : data[1]>=18
drinking_guys = list(filter(name,people))

for i in drinking_guys:
    print(i)
    
# functools.reduce(function,iterables)

import functools

letter = ["R","O","Y","A","L"]

name = lambda x,y : x+y
id = functools.reduce(name,letter)

print(id)