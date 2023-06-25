from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Cow(Animal):
    def eat(self):
        print("Cow eats grass.")
        
# class Human(Animal):
#     # def eat(self):
#         # print("Human eat rice.")
#     pass 
# Here there is class human can't instantiate with abstract method eat.

class Human(Animal):
    def eat(self):
        print("Human eat rice.")    
        
cow = Cow()
man = Human()
man.eat()
cow.eat()