class Bird:
    def fly(self):
        print("The bird is flying.")
        
class Ostrich(Bird):
    def fly(self): #method overriding
        print("The ostrich can't fly.")
        
ost = Ostrich()
ost.fly() 

# method chaining = to call different methods simultaneously

class Noodles:
    def open_packet(self):
        print("We open the packet.")
        return self
        
    def boil(self):
        print("Boil the noodles.")
        return self
        
    def add_taste_enhancer(self):
        print("Now, we add taste enhancer packets.")
        return self
        
    def eat_noodle(self):
        print("We eat the boiled noodle.")
        return self
    
waiwai =Noodles()
waiwai.open_packet()\
    .boil()\
    .add_taste_enhancer()\
    .eat_noodle()
    
# we can write it as waiwai.open_packet().boil().add_taste_enhancer().eat_noodle().Here, \ = line continuation