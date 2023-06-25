def large(text):
    return text.upper()

def small(text):
    return text.lower()

def hello(func):
    text = func("Hello World")
    print(text)
    
hello(large)
hello(small)


# for lambda function
# lambda parameter : expression
# Example => lambda x,y : x*y