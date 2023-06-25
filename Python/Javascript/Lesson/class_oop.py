# class [class name]:
#       pass

# create class in another file and import it
# from [file name] import [class name]

from bikes import Bike

bike_1 = Bike("Hero",2,1500,"Xpulse")
bike_2 = Bike("Honda",0.5,200,"XR")

print("The brand of bike is ", bike_1.name)
print("The bike is ", bike_1.age, "years old.")
print("The distance travelled on the bike is ",bike_1.distance, " km.")
print("The model of the bike is ", bike_1.model)

bike_1.driving()
bike_1.stop()

Bike.wheels =3
print(bike_1.wheels)