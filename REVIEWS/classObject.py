# Class can have method inside and attributes attach to objects created from the class

class Point:
    def __init__(self, value1, value2):
        self.x = value1
        self.y = value2
        print(f"Ponit x is {self.x} and point y is {self.y}")


    def show(self):
        print("This is a point")
    def exit(self):
        print("Exiting right now...")


point1 = Point(20, 25)
point1.show()
point1.exit()

point1.more = "More wealth coming..."
log = point1.more
print(log)

#Assign
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Defaul age is 18")
        print(f"You name is {self.name}, You are {self.age} years old")

    def talk(self):
        print("I can say all things in Igbo language")

person1 = Person("David", 30)
person1.level = "Graduate"
print(f"You are now a {person1.level}")

# inheritance
class Animal:
    def __init__(self, name, legs, winds, hands, fur, feathers):
        print(f"{name} has {legs} legs with {winds} wings, {hands} hands, {fur} Fur and {feathers} feathers")
    
    def noise(self):
        print("I makes alot of noise")


class Dog(Animal):
    def how(self):
        print("I bark a lot")

dog1 = Dog("Chizzy", 4, 0, 0, "Plenty", 0)
dog1.noise()



