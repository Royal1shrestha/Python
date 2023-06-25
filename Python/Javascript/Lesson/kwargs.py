def name(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hi ", end = " ")
    for key,value in kwargs.items():
        print(value, end = " ")
    
name(first="Royal",middle="God",last="Shrestha")