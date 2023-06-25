def announce(f):
    def cover():
        print("About to start .......")
        f()
        print("This is the end.")
    return cover
    
@announce
def body():
    print("Hello everybody!")
    
body()