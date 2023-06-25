# indexing[] : [start:stop:step]
# slicing() : (start,stop)

name = "Royal Shrestha"
print(name[0])
print(name[1:2])
print(name[:3])
print(name[5:])
print(name[0:14:2])
reverse_name = name[::-1]
print(reverse_name)

website1 = "http://google.com"
website2 = "http://yahoo.com"
# positive index starts at 0 and negative index starts at -1.
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])