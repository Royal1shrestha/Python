class Bike:
    
    wheels =2
    
    def __init__(self,name,age,distance,model):
        self.name = name #instant value
        self.age = age #instant value
        self.distance = distance #instant value
        self.model = model #instant value
        
    def driving(self):
        print("This "+self.model+" is driving.")
        
    def stop(self):
        print("This "+self.model+" has stopped.")