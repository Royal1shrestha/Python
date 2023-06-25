list=[{'name':'Dolphin','Species':'Mammal'},
      {'name':'Octopus','Species':'Pisces'},
      {'name':'Eagle','Species':'Birds'}
      ]

def arrange(list):
    return list["name"]

# list.sort(key=lambda list:list["Species"])
list.sort(key=arrange)

print(list)