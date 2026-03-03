#In object Oriented Programming the relationship between objects is important, and we are going to talk about two types of relationships between pbjects.
# Is-a and Has-a relationships
# Has-a example: A Company has a employess.
# IS-a example: A robot Dog is a robot, A robot Cat is a robot.
# the Is-a Relationship is also called as Inheritance.

#Lets see one exampleof Inheritance in python.
#In this Inheritance example we would have a general robot base class and then a robot dog and robot cat class that derive from that parent class.
#using inheritance it allows us to create a hierarchy of classes that shares a set of properties and methods.
#we do this by deriving a class from another class.
#the base class is also sometimes called the parent class
#and the derived class are sometimes called the child classes.

#some of the specific behaviours that the robot dog and robot cat classes have
# and which ones they have in common, othose are the ones that we are going to want to take out and put in the general robot class.
#we are moving he common behaviours to the general robot class, This will allows us to reuse code so we dont have to write same code over and over again.

#creating the parent robot class.
class robot:
    def __init__ (self, name):
        self.name = name
        self.position = [0,0]
        print("My Name is: ", self.name)
    def eat(self):
        print("I am hungry")
    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New Position:", self.position)
#To create a child class that derives from a parent class, we  put the parent class tha we were inheriting from in parentheses.
class robot_dog(robot):
    #we can also add our own init method here, but if we leave it out.
    #it will call the robot's init method by default.
    def bark(self):
        print("Woof Woof")
    def eat(self):
        super().eat()
        print("I like Bacon")
#here robot_dog is a child class and robot is the parent class, and robot_dog is inheriting from robot, so it has all the properties and methods of the robot class, and it also has its own bark method.
#main program
#now we have robot and robot_dog classes.
#now we are creating a robot_dog object.
my_robot_dog = robot_dog("Bud")
my_robot_dog.walk(5)
my_robot_dog.bark()


#By inheritance we can seamlessly the methods are called from either the parent class or the child class depending where the implementaion is.
#we saw that method called from parent class if it is not in child class.
#but what if the same method avalible in both the parent class and the child class.
my_robot_dog.eat()
#This is called method overridding. which allows us to customize a method's implementation in the child class.
#in this case the method in the child class will override the method in the parent class, so when we call that method on an object of the child class, it will use the method in the child class instead of the method in the parent class.
#if we also want to call the same method in the parent class along with the method in the child class, we can do that by using the super() function, which allows us to call a method from the parent class along with method in the child class.
