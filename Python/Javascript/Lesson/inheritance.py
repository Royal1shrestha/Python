# parent class
class Animal:
    alive = True
    
    def eat(self):
        print("The animal is eating.")
        
    def sleep(self):
        print("The animal is sleeping.")

# parent class
class Pisces:
    def swim(self):
        print("Pisces swim.")
        
# child class
class Human(Animal):
    def walk(self):
        print("Human can walk on two legs.")
        
# child class
class Snake(Animal):
    def crawl(self):
        print("Snake crawls.")
        
# derived child class/multilevel inheritance
class Cobra(Snake):
    def danger(self):
        print("The cobra is the second most poisonous venom snake.")
        
# multiple inheritance
class Goldfish(Animal, Pisces):
    pass

ram =Human()
python = Snake()
cob = Cobra()
fish = Goldfish()
ram.walk()
print(ram.alive)
python.sleep()
cob.crawl()
cob.eat()
fish.sleep()
fish.swim()