#Object-oreinted programming
#Designing computer programs to be organised around data or objects.

#why do we need object-oriented programming?
#As programs get larger and more complex, it's impossible for one person to understtand all of the complexity behind the program, so we need to break down the program into smaller pieces that are easier to understand and manage.
#In order for programmers to do very complicated things, such as develop robots or video games, it's helpful for them to think of related pieces of code as objects.
#we can think of an objects in terms of state and behaviour, the state of an object is the data that describes the object, and the behaviour of an object is the actions that the object can perform.
#objects have state and behaviour in real life and in object-oreinted programming as well.
#for example, a car is an object that has a state, which is the color of the car, the make and model of the car, and the year of the car.
#the behaviour of the car is the actions that the car can perform, such as starting the engine, accelerating, braking, and turning.

#defining a robot class
#Before we can create objects, we need to define a class.
#and then we can create instances of that class, which are also called objects.

#here we are going to create a robot_dog class and then we can create a  robot_dog object from that class.

class robot_dog():
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val
    def bark(self):
        print("Bow Bow!")

#creating an robot_dog object from the robot_dog class
my_dog = robot_dog("Rover", "Golden retriever")

print(my_dog.name)
print(my_dog.breed)

my_dog.bark()